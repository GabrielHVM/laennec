#!/usr/bin/env python3
import cv2 as cv
import numpy as np
from scipy.stats import entropy

from centroid import centroid_of_image

def asymmetry(binary_image, angle_variation):
    num_symmetry_axe = 0
    centroid_x, centroid_y = centroid_of_image(binary_image)
    centroid = (centroid_x, centroid_y)
    #angles = np.arange(0, 180, angle_variation)
    #print(angles)
    left_half = binary_image[:, :centroid_x]
    right_half = binary_image[:, centroid_x:]
    top_half = binary_image[:centroid_y, :]
    bottom_half = binary_image[centroid_y:, :]
    cv.imshow("left half", left_half)
    cv.imshow("right half", right_half)
    cv.imshow("top half", top_half)
    cv.imshow("bottom half", bottom_half)
    # Calculate entropy for the left and right halves
    left_entropy = entropy(left_half.flatten())
    right_entropy = entropy(right_half.flatten())

    # Calculate entropy for the top and bottom halves
    top_entropy = entropy(top_half.flatten())
    bottom_entropy = entropy(bottom_half.flatten())

    # Calculate the difference in entropy between left and right, and between top and bottom
    horizontal_entropy_diff = 1/(1+abs(left_entropy - right_entropy))
    vertical_entropy_diff = 1/(1+abs(top_entropy - bottom_entropy))

    print(horizontal_entropy_diff)
    print(vertical_entropy_diff)
    asymmetry_score = 0
    #if horizontal_entropy_diff >= 0.1:
    #    asymmetry_score = 0  # No asymmetry
    #elif not x_symmetric and y_symmetric:
    #    asymmetry_score = 1  # Asymmetry along X axis
    #elif not x_symmetric and not y_symmetric:
    #    asymmetry_score = 2  # Asymmetry along both X and Y axes
    #for angle in angles:
    #    rotation_matrix = cv.getRotationMatrix2D(centroid, angle, 1)
    #    rotated_image = cv.warpAffine(binary_image, rotation_matrix, binary_image.shape[::-1])
    #    cv.imshow("Rotated_image", rotated_image)
    #    cv.waitKey(0)
    #    left_half = rotated_image[:, :centroid_x]
    #    right_half = rotated_image[:, centroid_x:]
    #    print(np.array_equal(left_half, np.flip(right_half, axis=1)))
    #    if np.array_equal(left_half, np.flip(right_half, axis=1)):
    #        num_symmetry_axe += 1
    #if num_symmetry_axe == 0:
    #    asymmetry_score = 2
    #elif num_symmetry_axe == 1:
    #    asymmetry_score = 1
    #else:
    #    asymmetry_score = 0
    print(f"Asymmetry score: {asymmetry_score}")
    return asymmetry_score
