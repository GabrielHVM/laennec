from hair_detection import remove_hair
from cv2 import medianBlur, imshow, imread, bitwise_and, waitKey, imwrite


def _filter_with_median_filter(image):
    return medianBlur(image, 5)


def _segment_nevus_from_skin(image, nevus_maks):
    return bitwise_and(image, image, mask=nevus_maks)


def pre_process_image(image, nevus_mask):
    image_filtered = _filter_with_median_filter(image)
    nevus_image_segmented_from_skin = _segment_nevus_from_skin(image_filtered, nevus_mask)
    hair_removed = remove_hair(nevus_image_segmented_from_skin)
    return hair_removed


def pre_process_all_images(all_images, output_dir="../PH2Dataset/Pre Processed Images/"):
    for image_data in all_images:
        binary_mask_path = image_data['binary_mask']
        image_lesion_path = image_data['image_lesion']
        image_name_with_extension = image_lesion_path.split('/')[-1]
        image_lesion = imread(image_lesion_path)
        binary_mask = imread(binary_mask_path, 0)
        pre_processed_image = pre_process_image(image_lesion, binary_mask)
        complete_image_name = output_dir + image_name_with_extension
        imwrite(complete_image_name, pre_processed_image)
