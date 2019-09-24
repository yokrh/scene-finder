# coding: UTF-8

import sys
import os
import cv2
import numpy as np
import glob


dir_path = os.path.dirname(os.path.realpath(__file__)) + '/'
print(dir_path)
print(sys.argv[1:])

args = sys.argv
image_file_name = args[1]  # ex) video_luna.mp4_1002000.png
similarity_border = float(args[2])  # ex) 0.995


''''''
def calc_similarity(img1, img2):
    hsv1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
    hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

    scores, hists1, hists2 = [], [], []
    ch_names = {0: 'Hue', 1: 'Saturation', 2: 'Brightness'}
    for ch in ch_names:
        h1 = cv2.calcHist([hsv1], [ch], None, histSize=[256], ranges=[0, 256])
        h2 = cv2.calcHist([hsv2], [ch], None, histSize=[256], ranges=[0, 256])
        score = cv2.compareHist(h1, h2, cv2.HISTCMP_CORREL)
        hists1.append(h1)
        hists2.append(h2)
        scores.append(score)
    similarity_score = np.mean(scores)
    return similarity_score
''''''
''''''
def filter_similar_image_files(based_image_file, image_files, similarity_border):
    res = []
    based_img = cv2.imread(based_image_file, 1)
    for file in image_files:
        img = cv2.imread(file, 1)
        similarity_score = calc_similarity(based_img, img)
        print(file, similarity_score)
        if similarity_score > similarity_border:
            res.append(file)
    return res
''''''

based_frame_image_file = dir_path + '../../data/' + image_file_name
frame_image_dir = dir_path + '../../out/frame/'
target_frame_image_dir = dir_path + '../../out/target_frame/'

image_files = glob.glob(frame_image_dir + '*.png')
print('file length: ')
print(len(image_files))
similar_image_files = filter_similar_image_files(based_frame_image_file, image_files, similarity_border)

for file in similar_image_files:
    print(file)
    img = cv2.imread(file, 1)
    new_file = file.replace(frame_image_dir, target_frame_image_dir)
    cv2.imwrite(new_file, img)
