from hair_detection import remove_hair

def _filter_with_median_filter(image):
    return cv.medianBlur(image, 5)

def pre_process_image(image):
    image_filtered = _filter_with_median_filter(image)
    hair_removed = remove_hair(image)
    return remove_hair(image)
