#!/usr/bin/env python3
import cv2 as cv
import numpy as np
import math

from centroid import centroid_of_image


def _image_area(binary_image):
    contours, _ = cv.findContours(binary_image,
                                  cv.RETR_EXTERNAL,
                                  cv.CHAIN_APPROX_NONE)
    area = cv.contourArea(contours[0])
    return area


def _rotated_image(binary_image, center, angle):
    rotation_matrix = cv.getRotationMatrix2D(center=center,
                                             angle=angle, scale=1)
    return cv.warpAffine(binary_image,
                         rotation_matrix,
                         binary_image.shape)


def _assymetry_index(total_area, first_half_area, second_half_area, centroid_x):
    """Calculate asymmetry index given an image and x centoroid position."""
    return (abs(second_half_area - first_half_area)/total_area) * 100


def assymetry(binary_image, angle_variation=90):
    """Calculate asymmetry of a lesion."""
    centroid_x, centroid_y = centroid_of_image(binary_image)
    centroid = (centroid_x, centroid_y)

    rotated_image = _rotated_image(binary_image, centroid, angle_variation)

    top_half_image = rotated_image[:, centroid_x:]
    bottom_half_image = rotated_image[:, :centroid_x]
    left_half_image = binary_image[:, centroid_x:]
    right_half_image = binary_image[:, :centroid_x]

    total_area = _image_area(binary_image)
    top_half_area = _image_area(top_half_image)
    bottom_half_area = _image_area(bottom_half_image)
    left_half_area = _image_area(left_half_image)
    right_half_area = _image_area(right_half_image)

    return {"horizontal_assymetry_index": _assymetry_index(total_area,
                                                           right_half_area,
                                                           left_half_area,
                                                           centroid_x),
            "vertical_assymetry_index": _assymetry_index(total_area,
                                                         top_half_area,
                                                         bottom_half_area,
                                                         centroid_x)}


def _image_perimeter(binary_image):
    contours, _ = cv.findContours(binary_image,
                                  cv.RETR_EXTERNAL,
                                  cv.CHAIN_APPROX_NONE)
    return cv.arcLength(contours[0], True)


def _image_compactness(perimeter, area):
    return ((perimeter**2)/4*math.pi*area)


def border_irregularity(binary_image):
    """Calculate border irregularity."""
    area = _image_area(binary_image)
    perimeter = _image_perimeter(binary_image)
    return {"compactness": _image_compactness(perimeter, area)}


def color_variegation(lesion_image_segmented):
    """Calculate color varigation."""
    # Combination of features from skin pattern and ABCD analysis for lesion classification
    blue_channel, green_channel, red_channel = cv.split(lesion_image_segmented)
    blue_channel_standard_deviation = np.std(blue_channel, ddof=1)
    green_channel_standard_deviation = np.std(green_channel, ddof=1)
    red_channel_standard_deviation = np.std(red_channel, ddof=1)

    max_value_blue_channel = np.max(blue_channel)
    max_value_green_channel = np.max(green_channel)
    max_value_red_channel = np.max(red_channel)

    blue_channel_deviation = blue_channel_standard_deviation/max_value_blue_channel
    green_channel_deviation = green_channel_standard_deviation/max_value_green_channel
    red_channel_deviation = red_channel_standard_deviation/max_value_red_channel
    return {"blue_channel_deviation": blue_channel_deviation,
            "green_channel_deviation": green_channel_deviation,
            "red_channel_deviation": red_channel_deviation}


def abcd(lesion_binary_image, lesion_image_segmented):
    """Calcutes abcd from the lesion image."""
    return {"border_irregularity": border_irregularity(lesion_binary_image),
            "assymetry": assymetry(lesion_binary_image),
            "color_variegation": color_variegation(lesion_image_segmented)}
