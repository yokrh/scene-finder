# coding: UTF-8

import sys
import os
import cv2

dir_path = os.path.dirname(os.path.realpath(__file__)) + '/'
print(dir_path)
print(sys.argv[1:])

args = sys.argv
video_file_name = args[1]  # ex) video_luna.mp4


''''''
def capture_video_frame(video_file = 'video',
        output_dir='./',
        output_file_prefix='out_'):
    cap = cv2.VideoCapture(video_file)

    frame_num = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break

        img = frame  #img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        h = int(img.shape[0] / 2)
        w = int(img.shape[1] / 2)
        img = cv2.resize(img, (w, h))

        if frame_num % 100 == 0:
            file_name = output_dir + output_file_prefix + str(1000000 + frame_num) + '.png'
            cv2.imwrite(file_name, img)
            print(file_name)
        if frame_num > 4000:
            break
        frame_num += 1

    cap.release()
''''''

video_file = dir_path + '../../data/' + video_file_name
frame_image_dir = dir_path + '../../out/frame/'
frame_image_file_prefix = video_file_name + '_'

print('--- process begin ---')
print(video_file)
print(frame_image_dir)

capture_video_frame(video_file, frame_image_dir, frame_image_file_prefix)
print('--- process end ---')
