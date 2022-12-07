import numpy as np
import functools as fn

def equalize_histogram_of_color_image(image):
    hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    value_channel = hsv_image[:,:,2]
    value_equalized = cv.equalizeHist(value_channel)
    hsv_image[:,:,2] = value_equalized
    image_equalized_in_rgb = cv.cvtColor(hsv_image, cv.COLOR_HSV2BGR)
    return image_equalized_in_rgb

def rgb_2_yiq(image):
    #Y[i,j] = 0.299 * R[i,j] + 0.587 * G[i,j] + 0.114 * B[i,j]
    #I[i,j] = 0.5959 * R[i,j] + -0.2746 * G[i,j] + -0.3213 * B[i,j]
    #Q[i,j] = 0.2115 * R[i,j] + -0.5227 * G[i,j] + 0.3112 * B[i,j]
    image_shape = image.shape
    image_height = image_shape[0]
    image_width = image_shape[1]
    yiq_image = np.zeros((image_height, image_width, 3), dtype=np.uint8)
    for i in range(0, image_height-1):
        for j in range(0, image_width-1):
            yiq_image[i,j,0] = 0.299 * image[i,j,0] + 0.587 * image[i,j,1] + 0.144 * image[i,j,2]
            yiq_image[i,j,1] = 0.5959 * image[i,j,0] + -0.2746 * image[i,j,1] + -0.3213 * image[i,j,2]
            yiq_image[i,j,2] = 0.2115 * image[i,j,0] + -0.5227 * image[i,j,1] + 0.3112 * image[i,j,2]
    return yiq_image

#fn.reduce(function, sequence, initial)

def y_channel_of_yiq_from_rbg(image):
    #Y[i,j] = 0.299 * R[i,j] + 0.587 * G[i,j] + 0.114 * B[i,j]
    image_shape = image.shape
    image_height = image_shape[0]
    image_width = image_shape[1]
    y_channel = np.zeros((image_height, image_width), dtype=np.uint8)
    for i in range(0, image_height-1):
        for j in range(0, image_width-1):
            y_channel[i,j] = 0.299 * image[i,j,0] + 0.587 * image[i,j,1] + 0.144 * image[i,j,2]
    return y_channel