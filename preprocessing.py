import cv2
import numpy as np
#from PIL import Image

#image = Image.open('C:/Users/admin/Documents/Python-Scripts/OCR-scanner/uploads/test.png')
img = cv2.imread('C:/Users/admin/Documents/Python-Scripts/OCR-scanner/uploads/test.png')

# grey picture
def get_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(img):
    return cv2.medianBlur(img,5)

#thresholding
def thresholding(img):
    return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#dilation
def dilate(img):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(img, kernel, iterations = 1)

#erosion
def erode(img):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(img, kernel, iterations = 1)

#opening - erosion followed by dilation
def opening(img):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

#canny edge detection
def canny(img):
    return cv2.Canny(img, 100, 200)

#skew correction
def deskew(img):
    coords = np.column_stack(np.where(img > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

#template matching
def match_template(img, template):
    return cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
