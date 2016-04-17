from PIL import Image
import math
import sys

grayScaleChar = ('M','N','H','Q','$','O','C','?','7','>','!',':','-',';','.')

def imgToChar(sourceImg):
    width,height = sourceImg.size
    f = open('out.txt','w')
    for i in range(0,height,2):
        for j in range(width):
            avg = (sourceImg.getpixel((j,i))[0] + sourceImg.getpixel((j,i))[1] + sourceImg.getpixel((j,i))[2]) / 3
            grayScale = avg / 17;
            if grayScale > 14:
                grayScale = 14
            if grayScale < 0:
                grayScale = 0
            f.write(grayScaleChar[grayScale])
        f.write('\n')
    f.close()
    return

if __name__ == '__main__':
    if len(sys.argv) > 1 :
        sourceImg = Image.open(sys.argv[1])
        imgToChar(sourceImg)