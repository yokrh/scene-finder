# coding: UTF-8

import sys
import os
import glob
import cv2
import pyocr
import pyocr.builders
from PIL import Image as PilImage

dir_path = os.path.dirname(os.path.realpath(__file__)) + '/'
# print(dir_path)
# print(sys.argv[1:])

args = sys.argv
language = args[1]  # ex) 'eng', 'jpn'


''''''
def check_ocr_env():
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print('No OCR tool found')
        sys.exit(1)
    tool = tools[0]
    # print("Will use tool '%s'" % (tool.get_name()))
    langs = tool.get_available_languages()
    # print("Available languages: %s" % ", ".join(langs))

    return tool
''''''
''''''
def conv_to_pil(img):
    return PilImage.fromarray(img)
''''''
''''''
def conv_to_nparray(im_pil):
    return np.asarray(im_pil)
''''''

tool = check_ocr_env()
ocr_image_dir = dir_path + '../../out/ocr/'

# print('--- process begin ---')
res = '{'
image_files = glob.glob(ocr_image_dir + '*.png')
# print('file length: ' + str(len(image_files)))
for file in image_files:
    img = cv2.imread(file, 1)
    txt = tool.image_to_string(
        conv_to_pil(img),
        lang=language,
        builder=pyocr.builders.TextBuilder(tesseract_layout=6)
    ).replace('\n', '')
    res = res + '"' + file + '":"' + txt + '",'
res = res + '"dummy": "dummy"}'
print(res)
# print('--- process end ---')

