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

# Function to filter the image
def filter_with_median_filter(image):
    return cv.medianBlur(image, 5)

def bgr_to_gray(image):
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)

def get_struct_element(filter_size):
    filter = (filter_size, filter_size)
    return cv.getStructuringElement(cv.MORPH_RECT, filter)

def black_top_hat(image, struct_element_size):
    gray_scale_image = bgr_to_gray(image)
    struct_element = get_struct_element(struct_element_size)
    return cv.morphologyEx(gray_scale_image, cv.MORPH_BLACKHAT, struct_element)

def get_threshold(image):
    image_black_hat = black_top_hat(image, 17)
    return cv.threshold(image_black_hat, 10, 255, cv.THRESH_BINARY)

def inpaint(image):
    _,threshold = get_threshold(image)
    return cv.inpaint(image, threshold, 1, cv.INPAINT_TELEA)

def lesion_image(path):
    return cv.imread(path)

def binary_mask_of_lesion(path):
    return cv.imread(path, 0)

def region_of_lesion(lesion_image, lesion_binary_mask):
    return cv.bitwise_and(lesion_image, lesion_image, mask=lesion_binary_mask)

def equalize_histogram_of_color_image(image):
    hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    value_channel = hsv_image[:,:,2]
    value_equalized = cv.equalizeHist(value_channel)
    hsv_image[:,:,2] = value_equalized
    image_equalized_in_rgb = cv.cvtColor(hsv_image, cv.COLOR_HSV2BGR)
    return image_equalized_in_rgb

def pre_process_image(image):
    equalized_image = equalize_histogram_of_color_image(image)
    filtered_image = filter_with_median_filter(equalized_image)
    lesion_without_hair = inpaint(filtered_image)
    return lesion_without_hair


def main() -> None:
    images_path_prefix = \
        "/Users/gabriel.mata/Documents/tcc/laennec/PH2Dataset/PH2 Dataset images"
    list_complete_images_path = \
        complete_images_path(images_path_prefix)
    img_readed = cv.imread("/Users/gabriel.mata/Documents/tcc/laennec/PH2Dataset/PH2 Dataset images/IMD003/IMD003_Dermoscopic_Image/IMD003.bmp")
    binary_mask = cv.imread("/Users/gabriel.mata/Documents/tcc/laennec/PH2Dataset/PH2 Dataset images/IMD003/IMD003_lesion/IMD003_lesion.bmp", 0)
    pre_processed_image = pre_process_image(img_readed)
    lesion_pre_processed = region_of_lesion(pre_processed_image, binary_mask)
    lesion_raw_image = region_of_lesion(img_readed, binary_mask)
    cv.imshow("Resultado Pre-Processamento", cv.hconcat([lesion_raw_image, lesion_pre_processed]))
    cv.waitKey(0)

if __name__ == "__main__":
    main()