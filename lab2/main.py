from random import random
from PIL  import Image
from math import *

import matplotlib.pyplot as plt

def linear_contr(x, xmin, xmax):
    return int(((x-xmin)/(xmax-xmin)) * (255 - 0) + 0)

#import picture1 and convert it to L mode (only one component)
img      = Image.open("./image2.jpg")
img_data = img.convert("L").getdata()


# vars for hist
lst_x = list(range(256))
lst_y = [0] * 256
lst_y_new = [0] * 256

# calculate hist
for i in img_data:
    lst_y[i] += 1

#plot hist
plt.stem(lst_x, lst_y)
plt.show()

# equalization process
area_h    = img.size[0]*img.size[1]
average_h = area_h / 256.0

z       = 0
int_h   = 0
left  = [0] * 256
right = [0] * 256
new   = [0] * 256


lst_new = []

for j in range(255):
    left[j] = z
    int_h += lst_y[j]

    while int_h > average_h:
        int_h -= average_h
        z += 1

    right[j] = z

    #new[j] = right[j] - left[j]
    new[j] = int((right[j] + left[j])/2.0)

for i in img_data:
    if left[i] == right[i]:
        lst_new.append(left[i])
    else:
        #lst_new.append(int(new[i]*random()) + left[i])
        lst_new.append(new[i])

for i in lst_new:
    lst_y_new[i] += 1

plt.stem(lst_x, lst_y_new)
plt.show()

img_new = Image.new("L", img.size)
img_new.putdata(lst_new)
img_new.save("./image_new_hist.jpg")


#linear contrast
min = min(img_data)
max = max(img_data)

lst_new_lin = []
for i in img_data:
    lst_new_lin.append(linear_contr(i, min, max))


img_new = Image.new("L", img.size)
img_new.putdata(lst_new_lin)
img_new.save("./image_new_lin.jpg")


lst1 = []
lst2 = []
lst3 = []
lst4 = []
lst5 = []
lst6 = []
lst7 = []
lst8 = []

for i in img_data:
    temp = []
    for j in range(8):
        if i % 2 == 0:
            temp.append(0)
        else:
            temp.append(255)
        i /= 2
    lst1.append(temp[0])
    lst2.append(temp[1])
    lst3.append(temp[2])
    lst4.append(temp[3])
    lst5.append(temp[4])
    lst6.append(temp[5])
    lst7.append(temp[6])
    lst8.append(temp[7])

img_new = Image.new("L", img.size)
img_new.putdata(lst1)
img_new.save("./1.jpg")

img_new = Image.new("L", img.size)
img_new.putdata(lst2)
img_new.save("./2.jpg")

img_new = Image.new("L", img.size)
img_new.putdata(lst3)
img_new.save("./3.jpg")

img_new = Image.new("L", img.size)
img_new.putdata(lst4)
img_new.save("./4.jpg")

img_new = Image.new("L", img.size)
img_new.putdata(lst5)
img_new.save("./5.jpg")

img_new = Image.new("L", img.size)
img_new.putdata(lst6)
img_new.save("./6.jpg")

img_new = Image.new("L", img.size)
img_new.putdata(lst7)
img_new.save("./7.jpg")

img_new = Image.new("L", img.size)
img_new.putdata(lst8)
img_new.save("./8.jpg")