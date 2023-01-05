import cv2 as cv
import functools as fn
from utils import y_channel_of_yiq_from_rbg


def _get_struct_element(filter_size):
    filter = (filter_size, filter_size)
    return cv.getStructuringElement(cv.MORPH_RECT, filter)


def _black_top_hat(y_channel, struct_element_size):
    struct_element = _get_struct_element(struct_element_size)
    return cv.morphologyEx(y_channel, cv.MORPH_BLACKHAT, struct_element)


def _get_threshold(y_channel):
    image_black_hat = _black_top_hat(y_channel, 16)
    return cv.threshold(image_black_hat, 10, 255, cv.THRESH_BINARY)


def _inpaint(image, algorithm):
    print("Getting y channel from image")
    y_channel = y_channel_of_yiq_from_rbg(image)
    # y_channel_equalized = cv.equalizeHist(y_channel)
    print("Getting threshold from y_channel")
    _, threshold = _get_threshold(y_channel)
    print("Making inpaint in image with threshold and TELEA Algorithm")
    return cv.inpaint(image, threshold, 1.0, algorithm)


def remove_hair(image, algorithm=cv.INPAINT_TELEA):
    return _inpaint(image, algorithm)
