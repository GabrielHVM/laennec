import cv2 as cv
from functools import partial
import sys
import os

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
    image_path_prefix = path_prefix+ f'/{image_name}_Dermoscopic_Image'
    binary_mask_of_image_path_prefix = path_prefix+ f'/{image_name}_lesion'
    image_extension = ".bmp"
    complete_image_path = \
    construct_file_path(image_path_prefix,
                        image_name,
                        image_extension
                        )
    complete_binary_mask_path = \
    construct_file_path(binary_mask_of_image_path_prefix,
                        image_name+"_lesion",
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

def main() -> None:
    images_path_prefix = \
        "../PH2Dataset/PH2 Dataset images"
    list_complete_images_path = \
        complete_images_path(images_path_prefix)
    img_readed = cv.imread("../PH2Dataset/PH2 Dataset images/IMD003/IMD003_Dermoscopic_Image/IMD003.bmp")
    binary_mask = cv.imread("../PH2Dataset/PH2 Dataset images/IMD003/IMD003_lesion/IMD003_lesion.bmp", 0)
    cv.imshow("Resultado Pre-Processamento", cv.hconcat([lesion_raw_image, lesion_pre_processed]))
    cv.waitKey(0)

if __name__ == "__main__":
    main()