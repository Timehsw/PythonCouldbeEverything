# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/7/27.
'''

import pytesseract

from PIL import Image

# 打开一个图片
image=Image.open('test.png')

# 调用pytesseract的image_to_string方法识别出图片中的文字,返回识别出来的文字
text=pytesseract.image_to_string(image)

# 打印文字看看效果
print text
