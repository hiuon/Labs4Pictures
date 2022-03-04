from PIL  import Image
from math import *

#import picture1 and convert it to L mode (only one component)
img      = Image.open("./image.jpg")
img_data = img.convert("L").getdata()

# vars for hist
lst_x = list(range(256))
lst_y_new = [0] * 256
border = 240

img_data_new = []


#correct border value
while True:
    count_more = 0
    count_less = 0

    value_more = 0
    value_less = 0
    #print("Fix border value...:", border)
    for i in img_data:
        if i >= border:
            value_more += i
            count_more += 1
        else:
            value_less += i
            count_less += 1
    #print("more:", value_more/count_more, "less:", value_less/count_less)
    border_new = int(1/2 * (value_more/count_more + value_less/count_less))

    if abs(border_new - border) > 5:
        border = border_new
    else:
        break

#calculate new picture
for i in img_data:
    if i < border:
        img_data_new.append(0)
    else:
        img_data_new.append(255)

img_new = Image.new("L", img.size)
img_new.putdata(img_data_new)
img_new.save("./image_hist_border.jpg")


sum_grad = 0
sum = 0

for j in range(img.size[1]):
    for i in range(img.size[0]):
        grad_x = 0
        grad_y = 0
        if i + 1 == img.size[0]:
            grad_x = img_data[j * img.size[1] + i] - img_data[j * img.size[1] + i - 1]
        elif i - 1 < 0:
            grad_x = img_data[j * img.size[1] + i + 1] - img_data[j * img.size[1] + i]
        else:
            grad_x = img_data[j * img.size[1] + i + 1] - img_data[j * img.size[1] + i - 1]
        
        if j + 1 == img.size[1]:
            grad_y = img_data[j * img.size[1] + i] - img_data[(j - 1) * img.size[1] + i]
        elif j - 1 < 0:
            grad_y = img_data[(j + 1) * img.size[1] + i] - img_data[(j) * img.size[1] + i]
        else:
            grad_y = img_data[(j + 1) * img.size[1] + i] - img_data[(j - 1) * img.size[1] + i]
        
        if abs(grad_x) > abs(grad_y):
            sum_grad += grad_x
            sum += img_data[j * img.size[1] + i] * grad_x
        else:
            sum_grad += grad_y
            sum += img_data[j * img.size[1] + i] * grad_y

border_grad = int(sum/sum_grad)

img_data_grad = []
#calculate new picture
for i in img_data:
    if i < border_grad:
        img_data_grad.append(0)
    else:
        img_data_grad.append(255)

img_new = Image.new("L", img.size)
img_new.putdata(img_data_grad)
img_new.save("./image_grad_border.jpg")

# otsu
# calculate hist
length = len(img_data)
lst_hist = [0] * 256
lst_P1 = []
lst_mk = []
lst_sigma = []
m_G = 0

for i in img_data:
    lst_hist[i] += 1

for k in range(256):
    temp = 0
    temp_1 = 0
    for i in range(k + 1):
        temp += lst_hist[i] / length
        temp_1 += i * lst_hist[i] / length
    lst_P1.append(temp)
    lst_mk.append(temp_1)
    m_G += k * lst_hist[k] / length

#print(lst_P1)
#print(lst_mk)
#print(lst_hist)
#print(m_G)
sigma_max = 0
sigma_global = 0
border_otsu = 0
for k in range(256):
    sigma_global += pow(k - m_G, 2) * lst_hist[k] / length
    lst_sigma.append(pow(m_G * lst_P1[k] - lst_mk[k], 2)/(lst_P1[k]*(1 - lst_P1[k])))
    sigma = pow(m_G * lst_P1[k] - lst_mk[k], 2)/(lst_P1[k]*(1 - lst_P1[k]))
    if sigma > sigma_max:
        #print(k)
        border_otsu = k
        sigma_max = sigma

#print(border_otsu)
print(sigma_max/sigma_global)

img_data_otsu = []
#calculate new picture
for i in img_data:
    if i < border_otsu:
        img_data_otsu.append(0)
    else:
        img_data_otsu.append(255)

img_new = Image.new("L", img.size)
img_new.putdata(img_data_otsu)
img_new.save("./image_grad_otsu.jpg")