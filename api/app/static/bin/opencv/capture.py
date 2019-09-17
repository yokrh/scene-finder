# coding: UTF-8

import cv2

''''''
def capture_video_frame(video_file_path,
        output_dir='./',
        output_file_prefix='out_'):
    cap = cv2.VideoCapture(video_file_path)

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
            file_name = output_dir + output_file_prefix + str(10000000 + frame_num) + '.png'
            cv2.imwrite(file_name, img)
            print(file_name)
        if frame_num > 4000:
            break
        frame_num += 1

    cap.release()
''''''

video_file_path = '../../data/video.mp4'
frame_image_dir = '../../out/frame/'
frame_image_file_prefix = 'out_videomp4_'

capture_video_frame(video_file_path, frame_image_dir, frame_image_file_prefix)
