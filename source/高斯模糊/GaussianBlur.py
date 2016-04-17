#!/usr/bin/env python

from PIL import Image
import math
import sys

def getGaussMatrix(R, sigma):
    S = 2*R + 1;
    sum = 0
    matrix = [[0.0 for i in range(S)] for j in range(S)]  
    for i in range(S):
        for j in range(S):
            matrix[i][j] = 1 / ((2 * math.pi * sigma**2) * math.e**( ((i-R)**2 + (j-R)**2)/(2*(sigma**2))))
            sum += matrix[i][j]
    P = sum / 1.0;
    for i in range(2*R + 1):
        for j in range(2*R + 1):
            matrix[i][j] /= P
    return matrix

def imgBlur(sourceImg,matrix,R):
    width,height = sourceImg.size
    outImg = Image.new('RGB',sourceImg.size)
    for i in range(height):
        for j in range(width):
            outImg.putpixel([i,j],getPixelValue(sourceImg,matrix,i,j))
    return outImg

def getPixelValue(img,matrix,i,j):
    width,height = img.size
    valueRed = 0.0
    valueGreen = 0.0
    valueBlue = 0.0
    for ii in range(len(matrix)):
        for jj in range(len(matrix)):
            tempI = i + ( ii - (len(matrix)/2))
            tempJ = j + ( jj - (len(matrix)/2))
            if 0 <= tempI < height and 0 <= tempJ < width :
                valueRed += matrix[ii][jj] * img.getpixel((tempI,tempJ))[0]
                valueGreen += matrix[ii][jj] * img.getpixel((tempI,tempJ))[1]
                valueBlue += matrix[ii][jj] * img.getpixel((tempI,tempJ))[2]
            else:
                valueRed += matrix[ii][jj] * img.getpixel((i,j))[0]
                valueGreen += matrix[ii][jj] * img.getpixel((i,j))[1]
                valueBlue += matrix[ii][jj] * img.getpixel((i,j))[2]
    return (int(valueRed),int(valueGreen),int(valueBlue))

if __name__ == '__main__':
    if len(sys.argv) > 3 :
        sourceImg = Image.open(sys.argv[1])
        R = int(sys.argv[2])
        sigma = float(sys.argv[3])
    else:
        exit()

    matrix = getGaussMatrix(R, sigma)
    outImg = imgBlur(sourceImg,matrix,R)
    outImg.save( 'out.bmp','bmp')
