import cv2 as cv

def moments_of_image(binary_image):
    return cv.moments(binary_image)

def centroid_of_image(binary_image):
    moments = moments_of_image(binary_image)
    m00 = moments["m00"]
    m10 = moments["m10"]
    m01 = moments["m01"]
    center_x = int(m10/m00)
    center_y = int(m01/m00)
    return center_x, center_y

def draw_centroid_on_image(binary_image):
    centroid_x, centroid_y = centroid_of_image(binary_image)
    cv.circle(binary_image, (centroid_x, centroid_y), 4, (0,255,255), -1)
    cv.imshow("Centroid", binary_image)
    cv.waitKey(0)