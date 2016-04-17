from PIL import Image
import math

def f( x, y, z ):
    a = x * x + 9.0 / 4.0 * y * y + z * z - 1
    return a * a * a - x * x * z * z * z - 9.0 / 80.0 * y * y * z * z * z

def h( x, z ):
    y = 1.0
    while y > 0.0 :
        if f(x, y, z) <= 0.0:
            return y
        y = y-0.001
    return 0.0

width = 512
height = 512
img = Image.new('RGB',(width,height))

for sy in range (0, height):
    z = 1.5 - sy * 3.0 / height
    for sx in range (0, width):
        x = sx * 3.0 / width - 1.5
        v = f(x, 0.0, z)
        r = 0
        if v <= 0.0 :
             y0 = h(x, z)
             ny = 0.001
             nx = h(x + ny, z) - y0
             nz = h(x, z + ny) - y0
             nd = 1.0 / math.sqrt(nx * nx + ny * ny + nz * nz)
             d = (nx + ny - nz) / math.sqrt(3) * nd * 0.5 + 0.5
             r = d * 255.0
        img.putpixel([sx,sy],(int(r ),0,0))

img.show()
img.save( 'img.bmp','bmp')