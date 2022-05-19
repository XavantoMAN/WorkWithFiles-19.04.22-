import numpy as np
import numexpr as ne
from PIL import Image, ImageDraw

im = Image.new('RGB', (100,100), (128,128,128))
draw = ImageDraw.Draw(im)

X = np.arange(100)
print(X)
Y = ne.evaluate("X * X")
print(Y)
for x in X:
    draw.point((x, Y[x]), fill=(255,255,0))

im.show()


print('--------------------------------------')


s = '(2 + 5 + 6 + 7) * 2 / 3 * sin(3.14) / 2'
print(ne.evaluate(s))
