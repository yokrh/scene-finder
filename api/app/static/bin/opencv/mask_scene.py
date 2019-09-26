# coding: UTF-8

import sys
import os
import glob
import cv2
import numpy as np

dir_path = os.path.dirname(os.path.realpath(__file__)) + '/'
print(dir_path)
print(sys.argv[1:])

args = sys.argv
background_color = int(args[1])  # ex) 0:black, 255:white
hsv_min_h = int(args[2])  # ex) 0, 0
hsv_min_s = int(args[3])  # ex) 0, 0
hsv_min_v = int(args[4])  # ex) 0, 50
hsv_max_h = int(args[5])  # ex) 0, 255
hsv_max_s = int(args[6])  # ex) 0, 255
hsv_max_v = int(args[7])  # ex) 160, 255

hsv_min = (hsv_min_h, hsv_min_s, hsv_min_v)
hsv_max = (hsv_max_h, hsv_max_s, hsv_max_v)
reverse_color_flg = True if background_color < 100 else False


''''''
def mask_to_color(img, color=255, hsv_min=(255,255,255), hsv_max=(255,255,255)):
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(
        hsv_img,
        np.array(hsv_min, np.uint8),
        np.array(hsv_max, np.uint8)
    )
    inv_mask = cv2.bitwise_not(mask)
    color_full = np.full(img.shape, color, dtype=img.dtype)
    background = cv2.bitwise_and(color_full, color_full, mask=mask)
    extracted = cv2.bitwise_and(img, img, mask=inv_mask)
    return cv2.add(extracted, background)
''''''
''''''
def add_color_margin(img, color=255, h_margin=10, w_margin=10):
    h, w = img.shape[0], img.shape[1]
    shape = [h + h_margin, w + w_margin]
    color_full = np.full((shape[0], shape[1], 3), color, dtype=img.dtype)

    hb = int(h_margin / 2)
    he = int(h_margin / 2) + h
    wb = int(w_margin / 2)
    we = int(w_margin / 2) + w
    centered_img = color_full
    centered_img[hb:he, wb:we] = img

    return centered_img
''''''
''''''
def reverse_black_and_white(img):
    return cv2.bitwise_not(img)
''''''

trimmed_image_dir = dir_path + '../../out/trimmed/'
ocr_image_dir = dir_path + '../../out/ocr/'

image_files = glob.glob(trimmed_image_dir + '*.png')
for file in image_files:
    img = cv2.imread(file, 1)
    img = mask_to_color(img, background_color, hsv_min, hsv_max)
    img = add_color_margin(img, background_color)
    if reverse_color_flg:
        img = reverse_black_and_white(img)
    cv2.imwrite(file.replace(trimmed_image_dir, ocr_image_dir), img)
