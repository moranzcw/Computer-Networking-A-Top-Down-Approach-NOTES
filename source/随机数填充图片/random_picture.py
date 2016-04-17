from PIL import Image
import random
import os

width = 4000
height = 3000

img = Image.new('RGB',(width,height))

for i in range (0,width):
	for j in range (0,height):
		img.putpixel([i,j],(random.randint(0,255),
			random.randint(0,255),
			random.randint(0,255)))

img.show()
img.save( 'img.bmp','bmp')