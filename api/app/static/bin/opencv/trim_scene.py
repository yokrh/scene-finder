# coding: UTF-8

import sys
import os
import glob
import cv2

dir_path = os.path.dirname(os.path.realpath(__file__)) + '/'
print(dir_path)
print(sys.argv[1:])

args = sys.argv
top = float(args[1])  # ex) 0.15
bottom = float(args[2])  # ex) 0.2
left = float(args[3])  # ex) 0.55
right = float(args[4])  # ex) 0.65


''''''
def trim_image(img, h_begin=0.1, h_end=0.2, w_begin=0, w_end=1):
    h = img.shape[0]
    w = img.shape[1]

    hb = int (h_begin * h)
    he = int (h_end * h)
    wb = int (w_begin * w)
    we = int (w_end * w)

    return img[hb:he, wb:we]
''''''

target_frame_image_dir = dir_path + '../../out/target_frame/'
trimmed_image_dir = dir_path + '../../out/trimmed/'

image_files = glob.glob(target_frame_image_dir + '*.png')
print('file length: ')
print(len(image_files))
for file in image_files:
    img = cv2.imread(file, 0)
    img = trim_image(img, top, bottom, left, right)
    cv2.imwrite(file.replace(target_frame_image_dir, trimmed_image_dir), img)
