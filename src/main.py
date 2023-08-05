import cv2 as cv
import numpy as np
from functools import partial
import sys
import os

from pre_process_image import pre_process_all_images
from centroid import draw_centroid_on_image, centroid_of_image
from abcd import asymmetry

def list_files_in_path(path):
    directories_list = os.listdir(path)
    return directories_list


def get_images_name(images_dir):
    return list_files_in_path(images_dir)


def construct_file_path(path, filename, extension):
    file_path = path + f'/{filename}' + extension
    return file_path


def construct_complete_image_path(image_prefix_path, image_name):
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
    partial_construct_complete_image_path = \
        partial(construct_complete_image_path, images_prefix_path)
    list_images_path = list(map(partial_construct_complete_image_path,
                                images_name))
    return list_images_path


def complete_images_path(images_dir):
    images_name = get_images_name(images_dir)
    completed_images_path = \
        list_complete_image_path(images_dir, images_name)
    return completed_images_path


def show_image(src):
    img = cv.imread(src)
    if img is None:
        sys.exit("Could not read the image.")
    cv.imshow("Nevus image", img)
    cv.waitKey(0)


def lesion_image(path):
    return cv.imread(path)


def binary_mask_of_lesion(path):
    return cv.imread(path, 0)

def translate_image_to_center(binary_image):
    centroid_x, centroid_y = centroid_of_image(binary_image)
    height, width = binary_image.shape[:2]
    translation_x = (width // 2) - centroid_x
    translation_y = (height // 2) - centroid_y

    # Crie uma matriz de transformação para fazer o deslocamento
    translation_matrix = np.float32([[1, 0, translation_x], [0, 1, translation_y]])

    # Aplique o deslocamento para transladar a lesão para o centro da imagem
    translated_image = cv.warpAffine(binary_image, translation_matrix, (width, height))
    cv.imshow("Imagem centralizada",translated_image)
    #cv.waitKey(0)


def main() -> None:
    images_path_prefix = \
        "../PH2Dataset/PH2 Dataset images"
    all_images_path = \
        complete_images_path(images_path_prefix)

    binary_mask_path = all_images_path[0]["binary_mask"]
    image_name = "IMD064"
    binary_mask_path = f"../PH2Dataset/PH2 Dataset images/{image_name}/{image_name}_lesion/{image_name}_lesion.bmp"
    #print(all_images_path)
    #pre_process_all_images(all_images_path)

    print(binary_mask_path)
    binary_mask = (cv.imread(binary_mask_path, 0))
    translate_image_to_center(binary_mask)
    draw_centroid_on_image(binary_mask)
    #asymmetry(binary_mask, 180)
    #cv.imshow("BINARY MASK",binary_mask)
    #cv.waitKey(0)

if __name__ == "__main__":
    main()
