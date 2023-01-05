import numpy as np
import functools as fn
import cv2 as cv


def equalize_histogram_of_color_image(image):
    hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    value_channel = hsv_image[:, :, 2]
    value_equalized = cv.equalizeHist(value_channel)
    hsv_image[:, :, 2] = value_equalized
    image_equalized_in_rgb = cv.cvtColor(hsv_image, cv.COLOR_HSV2BGR)
    return image_equalized_in_rgb


def y_channel_of_yiq_from_rbg(image):
    r_channel = image[:, :, 0] * 0.299
    g_channel = image[:, :, 1] * 0.587
    b_channel = image[:, :, 2] * 0.144
    y_channel = np.array(r_channel + g_channel + b_channel, dtype=np.uint8)
    return y_channel
