from PIL  import Image
from math import *

#import picture1 and convert it to L mode (only one component)
img      = Image.open("./image.jpg")
img_data = img.convert("L").getdata()

lst_mask = [[1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1]]
coef = 0
for i in range(len(lst_mask)):
    for j in range(len(lst_mask[i])):
        coef += lst_mask[i][j]

lst_mask_gauss = [[1, 2, 1],
                  [2, 4, 2],
                  [1, 2, 1]]
coef_gauss = 0
for i in range(len(lst_mask_gauss)):
    for j in range(len(lst_mask_gauss[i])):
        coef_gauss += lst_mask_gauss[i][j]

lst_mask_laplas = [[0,  1, 0],
                   [1, -4, 1],
                   [0,  1, 0]]
coef_laplas = 0
for i in range(len(lst_mask_laplas)):
    for j in range(len(lst_mask_laplas[i])):
        coef_gauss += lst_mask_laplas[i][j]



lst_lin_filt = []
lst_gauss_filt = []
lst_laplas_filt = []
# linear filter
for j in range(img.size[1]):
    for i in range(img.size[0]):
        pixel = 0
        for mask_j in range(len(lst_mask)):
            for mask_i in range(len(lst_mask[mask_j])):
                try:
                    pixel += img_data[(j - floor(len(lst_mask)/2) + mask_j)*img.size[1] + i - floor(len(lst_mask[mask_j])/2) + mask_i]*lst_mask[mask_j][mask_i]
                except IndexError:
                    pixel += img_data[j*img.size[1] + i]*lst_mask[mask_j][mask_i]
        pixel /= coef
        lst_lin_filt.append(int(pixel))

img_new = Image.new("L", img.size)
img_new.putdata(lst_lin_filt)
img_new.save("./image_lin_filter.jpg")

#gauss filter
for j in range(img.size[1]):
    for i in range(img.size[0]):
        pixel = 0
        for mask_j in range(len(lst_mask_gauss)):
            for mask_i in range(len(lst_mask_gauss[mask_j])):
                try:
                    pixel += img_data[(j - floor(len(lst_mask_gauss)/2) + mask_j)*img.size[1] + i - floor(len(lst_mask_gauss[mask_j])/2) + mask_i]*lst_mask_gauss[mask_j][mask_i]
                except IndexError:
                    pixel += img_data[j*img.size[1] + i]*lst_mask_gauss[mask_j][mask_i]
        pixel /= coef_gauss
        lst_gauss_filt.append(int(pixel))

img_new = Image.new("L", img.size)
img_new.putdata(lst_gauss_filt)
img_new.save("./image_gauss_filter.jpg")

#laplasian
for j in range(img.size[1]):
    for i in range(img.size[0]):
        pixel = img_data[j*img.size[1] + i]
        for mask_j in range(len(lst_mask_laplas)):
            for mask_i in range(len(lst_mask_laplas[mask_j])):
                try:
                    pixel -= img_data[(j - floor(len(lst_mask_laplas)/2) + mask_j)*img.size[1] + i - floor(len(lst_mask_laplas[mask_j])/2) + mask_i]*lst_mask_laplas[mask_j][mask_i]
                except IndexError:
                    pixel -= img_data[j*img.size[1] + i]*lst_mask_laplas[mask_j][mask_i]
        lst_laplas_filt.append(int(pixel))

img_new = Image.new("L", img.size)
img_new.putdata(lst_laplas_filt)
img_new.save("./image_laplas_filter.jpg")

#нерезкое маскирование
lst_mask_g = []
for i in range(img.size[1]*img.size[0]):
    lst_mask_g.append(img_data[i] - lst_lin_filt[i])
lst_g_filt = []
for i in range(img.size[1]*img.size[0]):
    lst_g_filt.append(img_data[i] + int(lst_mask_g[i]))
img_new = Image.new("L", img.size)
img_new.putdata(lst_g_filt)
img_new.save("./image_g_filter.jpg")

#median
window_x = 3
window_y = 3
lst_median_filt = []
lst_median_min_filt = []
lst_median_max_filt = []
for j in range(img.size[1]):
    for i in range(img.size[0]):
        temp = []
        for mask_j in range(window_y):
            for mask_i in range(window_x):
                try:
                    temp.append(img_data[(j - floor(window_y/2) + mask_j)*img.size[1] + i - floor(window_x/2) + mask_i])
                except IndexError:
                    temp.append(img_data[(j)*img.size[1] + i])
        temp.sort()
        lst_median_filt.append(temp[floor(window_x*window_y/2)])
        lst_median_max_filt.append(temp[-1])
        lst_median_min_filt.append(temp[0])

img_new = Image.new("L", img.size)
img_new.putdata(lst_median_filt)
img_new.save("./image_median_filter.jpg")

img_new = Image.new("L", img.size)
img_new.putdata(lst_median_max_filt)
img_new.save("./image_median_max_filter.jpg")

img_new = Image.new("L", img.size)
img_new.putdata(lst_median_min_filt)
img_new.save("./image_median_min_filter.jpg")


