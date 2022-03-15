from PIL  import Image, ImageStat
from math import *

#import picture1 and convert it to L mode (only one component)
img      = Image.open("./image.jpg")
img_data = img.convert("L").getdata()
max_bright = max(img_data)
board = int(0.7*max_bright)

coef_laplas = 0
lst_mask_point = [[1,  1, 1],
                   [1, -8, 1],
                   [1,  1, 1]]
lst_point_filt = []

lst_mask_line_horz = [[1,  0, -1],
                   [1, 0, -1],
                   [1,  0, -1]]
lst_line_horz_filt = []   

lst_mask_move = [[0,  -1, 0],
                   [0, 1, 0],
                   [0,  0, 0]]
lst_line_move = []   

for j in range(img.size[0]):
    for i in range(img.size[1]):
        pixel = 0
        for mask_j in range(len(lst_mask_point)):
            for mask_i in range(len(lst_mask_point[mask_j])):
                try:
                    pixel -= img_data[(j - floor(len(lst_mask_point)/2) + mask_j)*img.size[0] + i - floor(len(lst_mask_point[mask_j])/2) + mask_i]*lst_mask_point[mask_j][mask_i]
                except IndexError:
                    pixel -= img_data[j*img.size[0] + i]*lst_mask_point[mask_j][mask_i]
        if abs(pixel) > board:
            lst_point_filt.append(255)
        else:
            lst_point_filt.append(0)

img_new = Image.new("L", img.size)
img_new.putdata(lst_point_filt)
img_new.save("./image_points.jpg")


im = Image.open("./image3.jpg")
px = im.convert("L")
px_1 = px.copy()
px1 = px_1.load()
for i in range(px.size[0]):
    for j in range(px.size[1]):
        pixel = 0
        for mask_i in range(len(lst_mask_line_horz)):
            for mask_j in range(len(lst_mask_line_horz[mask_i])):
                try:
                    pixel -= px1[i - floor(len(lst_mask_line_horz)/2) + mask_i, j - floor(len(lst_mask_line_horz[mask_i])/2) + mask_j]*lst_mask_line_horz[mask_i][mask_j]
                except IndexError:
                    pixel -= px1[i, j]*lst_mask_line_horz[mask_i][mask_j]
        if abs(pixel) > 400:
            px1[i, j] = (255)
        else:
            px1[i, j] = (0)
px_1.save("./image_lines_horz.jpg")


img = Image.open("./image6.jpg")
px = img.convert("L")
px_1 = px.copy()
px1 = px_1.load()


lst_mask_kirsh = [[3,  3, 3],
                      [3, 0, 3],
                      [-5,  -5, -5]]
lst_line_horz_filt = [] 
for i in range(px.size[0]):
    for j in range(px.size[1]):
        pixel = 0
        for mask_i in range(len(lst_mask_kirsh)):
            for mask_j in range(len(lst_mask_kirsh[mask_i])):
                try:
                    pixel -= px1[i - floor(len(lst_mask_kirsh)/2) + mask_i, j - floor(len(lst_mask_kirsh[mask_i])/2) + mask_j]*lst_mask_kirsh[mask_i][mask_j]
                except IndexError:
                    pixel -= px1[i, j]*lst_mask_kirsh[mask_i][mask_j]
        if abs(pixel) > 600:
            px1[i, j] = (255)
        else:
            px1[i, j] = (0)
px_1.save("./image_kirsh.jpg")