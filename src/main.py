import cv2 as cv
import numpy as np
import pandas as pd
from functools import partial
import sys
import os
import abcd

from centroid import centroid_of_image
from pre_process_image import pre_process_image


def list_files_in_path(path):
    """List files in path."""
    directories_list = os.listdir(path)
    return directories_list


def get_images_name(images_dir):
    """Get images name."""
    return list_files_in_path(images_dir)


def construct_file_path(path, filename, extension):
    """Construct file path."""
    file_path = path + f'/{filename}' + extension
    return file_path


def construct_complete_image_path(image_prefix_path, image_name):
    """Construct complete image path."""
    path_prefix = image_prefix_path + f'/{image_name}'
    image_path_prefix = path_prefix + f'/{image_name}_Dermoscopic_Image'
    binary_mask_of_image_path_prefix = path_prefix + f'/{image_name}_lesion'
    image_extension = ".bmp"
    complete_image_path = \
        construct_file_path(image_path_prefix,
                            image_name,
                            image_extension
                            )
    complete_binary_mask_path = \
        construct_file_path(binary_mask_of_image_path_prefix,
                            image_name + "_lesion",
                            image_extension)
    return {"image_lesion": complete_image_path,
            "binary_mask": complete_binary_mask_path}


def list_complete_image_path(images_prefix_path, images_name):
    """List complete image path."""
    partial_construct_complete_image_path = \
        partial(construct_complete_image_path, images_prefix_path)
    list_images_path = list(map(partial_construct_complete_image_path,
                                images_name))
    return list_images_path


def complete_images_path(images_dir):
    """Complete images path."""
    images_name = get_images_name(images_dir)
    completed_images_path = \
        list_complete_image_path(images_dir, images_name)
    return completed_images_path


def show_image(src):
    """Show a image."""
    img = cv.imread(src)
    if img is None:
        sys.exit("Could not read the image.")
    cv.imshow("Nevus image", img)
    cv.waitKey(0)


def translate_image_to_center(binary_image):
    """Translate image to center."""
    centroid_x, centroid_y = centroid_of_image(binary_image)
    height, width = binary_image.shape[:2]
    translation_x = (width // 2) - centroid_x
    translation_y = (height // 2) - centroid_y

    # Crie uma matriz de transformação para fazer o deslocamento
    translation_matrix = np.float32([[1, 0, translation_x],
                                     [0, 1, translation_y]])

    # Aplique o deslocamento para transladar a lesão para o centro da imagem
    translated_image = cv.warpAffine(binary_image,
                                     translation_matrix,
                                     (width, height))
    return translated_image


def main() -> None:
    """Execute main module's function."""
    lesions_database_features_path = "../PH2Dataset/PH2_dataset.xlsx"
    data = pd.read_excel(lesions_database_features_path, header=12)
    for _, row in data.iterrows():
        image_name = row["Image Name"]
        lesion_image_path = f"../PH2Dataset/PH2 Dataset images/{image_name}/{image_name}_Dermoscopic_Image/{image_name}.bmp"
        lesion_binary_image_path = f"../PH2Dataset/PH2 Dataset images/{image_name}/{image_name}_lesion/{image_name}_lesion.bmp"
        lesion_image = cv.imread(lesion_image_path, cv.IMREAD_COLOR)
        lesion_binary_image = cv.imread(lesion_binary_image_path, 0)
        lesion_image_pre_processed = pre_process_image(lesion_image, lesion_binary_image)
        abcd_features = abcd.abcd(lesion_binary_image, lesion_image_pre_processed)
        print(row["Image Name"])
        print(row["Asymmetry\n(0/1/2)"])
        print(abcd_features)
        break


if __name__ == "__main__":
    main()
