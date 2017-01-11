import os
import re
import sys
import PIL
import numpy as np
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def erase_null(path):
    fs = os.listdir(path)
    nd = np.array(Image.open('%s/0.png'%(path)))
    for f in fs:
        if f == '0.png':
            continue
        data = np.array(Image.open('%s/%s'%(path,f)))
        if np.array_equal(nd,data):
            print('%s/%s'%(path,f))
            os.remove('%s/%s'%(path,f))

def erase_white(path):
    fs = os.listdir(path)
    for f in fs:
        data = np.array(Image.open('%s/%s'%(path,f)))
        if data.sum() == data.size * 255:
            print('%s/%s'%(path,f))
            os.remove('%s/%s'%(path,f))

if __name__ == '__main__':
    erase_white(sys.argv[1])
    erase_null(sys.argv[1])
