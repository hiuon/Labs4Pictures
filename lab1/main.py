from PIL import Image
from math import *

#constants
plus_value = -100
multiply_value = 1.9
gamma_const = 2
c_const_log = 100
c_const = 1


#lists of pixels
lst_plus = []
lst_multiply = []
lst_neg = []
lst_log = []
lst_step = []

#import picture1 and convert it to L mode (only one component)
img = Image.open("./image.jpg")
img_data = img.convert("L").getdata()

#import picture2 and convert it to L mode (only one component)
img2 = Image.open("./image3.jpg")
img2_data = img2.convert("L").getdata()

#add constant
for i in img_data:
    if i + plus_value > 255:
        lst_plus.append(255)
    elif i + plus_value < 0:
        lst_plus.append(0)
    else:
        lst_plus.append(i + plus_value)

#mult constant
for i in img_data:
    if i * multiply_value > 255:
        lst_multiply.append(255)
    elif i * multiply_value < 0:
        lst_multiply.append(0)
    else:
        lst_multiply.append(int(i * multiply_value))

#neg
for i in img_data:
    lst_neg.append(256 - 1 - i)

#log
for i in img2_data:
    lst_log.append(int(c_const_log*log10(1 + i)))

#step
for i in img2_data:
    lst_step.append(int(c_const*pow(i, gamma_const)))

img_plus = Image.new("L", img.size)
img_plus.putdata(lst_plus)
img_plus.save("./image_plus.jpg")

img_mult = Image.new("L", img.size)
img_mult.putdata(lst_multiply)
img_mult.save("./image_mult.jpg")

img_neg = Image.new("L", img.size)
img_neg.putdata(lst_neg)
img_neg.save("./image_neg.jpg")

img_log = Image.new("L", img2.size)
img_log.putdata(lst_log)
img_log.save("./image_log.jpg")

img_step = Image.new("L", img2.size)
img_step.putdata(lst_step)
img_step.save("./image_step.jpg")