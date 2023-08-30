#!/usr/bin/env python3
import cv2 as cv
import numpy as np
#from scipy.stats import entropy

from centroid import centroid_of_image

def _assymetry_index(binary_image, centroid_x):
    left_half = binary_image[:, :centroid_x]/255
    right_half = binary_image[:, centroid_x:]/255
    left_half_area = np.sum(left_half)
    right_half_area = np.sum(right_half)
    total_area = left_half_area + right_half_area
    delta_area = abs(left_half_area - right_half_area)
    return (delta_area/total_area) * 100

def asymmetry(binary_image, angle_variation=180):
    centroid_x, centroid_y = centroid_of_image(binary_image)
    centroid = (centroid_x, centroid_y)
    rotation_matrix = cv.getRotationMatrix2D(center=centroid, angle=angle_variation, scale=1)
    rotate_image = cv.warpAffine(binary_image, rotation_matrix, binary_image.shape[::-1])
    return {"horizontal_assymetry_index" : _assymetry_index(binary_image, centroid_x),
            "vertical_asymmetry_index" : _assymetry_index(rotate_image, centroid_x)}

def border_irregularity(binary_image):
    binary_image_normalized = binary_image/255
    lesion_contours, _ = cv.findContours(binary_image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    #cv.imshow("lesion_contours",lesion_contours[0])
    cv.drawContours(binary_image_normalized, lesion_contours, -1, (0,255,0), 3)
    cv.imshow("binary_image_normalized", binary_image_normalized)
    cv.waitKey(0)
    my_area = np.sum(binary_image_normalized)
    print(my_area)
    lesion_area = cv.contourArea(lesion_contours[0])
    print(lesion_area)
    return None
