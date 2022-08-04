import math
from PIL import Image, ImageDraw

w, h = 220, 200

img = Image.new("RGB", (w,h))

img1 = ImageDraw.Draw(img)

count = 0
for i in range(5):
    count += 1

    shape = [(5 + count, 200), (5 + count, 0)]

    img1.line(shape, fill="#ffff33")


img.show()



