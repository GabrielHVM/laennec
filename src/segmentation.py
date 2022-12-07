from cv2 import bitwise_and

def nevus_segmeted_from_skin(nevus_image, nevus_binary_mask):
    bitwise_and(lesion_image, lesion_image, mask=lesion_binary_mask)
    pass