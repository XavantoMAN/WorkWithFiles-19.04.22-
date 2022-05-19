import re
import numexpr as ne
import numpy as np
from PIL import Image, ImageDraw
import math
im = Image.new('RGB', (100,100), (128,128,128))
draw = ImageDraw.Draw(im)
file = open('text.txt', 'r')
mass = []
k = 2
x = np.arange(1,10)
b = 4
a = 1
c = 3
d = 7
n = 5
e = math.e 

while True:
    line = file.readline()
    line = re.sub('\n','',line)
    if not line:
        break

    s = line.split(':')
    s = s[1].split(';')
    for i in s:
        list1 = i.split('= ')
        mass.append(list1[1])
        
for i in mass:
    print(ne.evaluate(i))
    Y = ne.evaluate(i)
    s = list(Y)
    print(s)
    for _x in x:
        draw.point((_x-1, Y[_x-1]), fill=(255,0,0))

im.show()        



