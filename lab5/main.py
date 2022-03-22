from PIL  import Image
from math import *

#import picture1 and convert it to L mode (only one component)
img      = Image.open("./image.jpg")
img_data = img.convert("L").getdata()
max_bright = max(img_data)
board = int(0.9*max_bright)

coef_laplas = 0
lst_mask_point = [ [1,  1, 1],
                   [1, -8, 1],
                   [1,  1, 1]]
lst_point_filt = []

lst_mask_line_previt = [[1, 1, 1],
                        [0, 0, 0],
                        [-1, -1, -1]]
lst_line_previt = []

lst_mask_move = [[0, -1, 0],
                 [0,  1, 0],
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


max_bright = 0
min_bright = 1000

im = Image.open("./image5.jpg")
px = im.convert("L")
px_1 = px.copy()
px1 = px_1.load()
lst_grad_previt = []
for i in range(px.size[0]):
    lst_grad_previt.append([])
    for j in range(px.size[1]):
        pixel = 0
        for mask_i in range(len(lst_mask_line_previt)):
            for mask_j in range(len(lst_mask_line_previt[mask_i])):
                try:
                    pixel -= px1[i - floor(len(lst_mask_line_previt)/2) + mask_i, j - floor(len(lst_mask_line_previt[mask_i])/2) + mask_j]*lst_mask_line_previt[mask_i][mask_j]
                except IndexError:
                    pixel -= px1[i, j]*lst_mask_line_previt[mask_i][mask_j]
        if max_bright < abs(pixel):
            max_bright = abs(pixel)
        if min_bright > abs(pixel):
            min_bright = abs(pixel)
        lst_grad_previt[i].append(abs(pixel))
        # if abs(pixel) > 400:
        #     px1[i, j] = (255)
        # else:
        #     px1[i, j] = (0)
# max_bright = max(lst_line_previt)*0.8

for i in range(px.size[0]):
    for j in range(px.size[1]):
        if lst_grad_previt[i][j] > max_bright*0.7:
            px1[i, j] = (255)
        else:
            px1[i, j] = (0)


px_1.save("./image_lines_previt.jpg")

max_bright = 0
min_bright = 1000
px_1 = px.copy()
px1 = px_1.load()
lst_grad_move = []
for i in range(px.size[0]):
    lst_grad_move.append([])
    for j in range(px.size[1]):
        pixel = 0
        for mask_i in range(len(lst_mask_move)):
            for mask_j in range(len(lst_mask_move[mask_i])):
                try:
                    pixel -= px1[i - floor(len(lst_mask_move)/2) + mask_i, j - floor(len(lst_mask_move[mask_i])/2) + mask_j]*lst_mask_move[mask_i][mask_j]
                except IndexError:
                    pixel -= px1[i, j]*lst_mask_move[mask_i][mask_j]
        if max_bright < abs(pixel):
            max_bright = abs(pixel)
        if min_bright > abs(pixel):
            min_bright = abs(pixel)
        lst_grad_move[i].append(abs(pixel))
        # if abs(pixel) > 250:
        #     px1[i, j] = (255)
        # else:
        #     px1[i, j] = (0)

for i in range(px.size[0]):
    for j in range(px.size[1]):
        if lst_grad_move[i][j] > max_bright*0.7:
            px1[i, j] = (255)
        else:
            px1[i, j] = (0)
# max_bright = max(lst_line_move)*0.8
# for i in range(px.size[0]):
#     for j in range(px.size[1]):
#         if lst_line_move[i*px.size[0] + j] > max_bright:
#             px1[i, j] = (255)
#         else:
#             px1[i, j] = (0)

px_1.save("./image_lines_move.jpg")


img = Image.open("./image6.jpg")
px = img.convert("L")
px_1 = px.copy()
px1 = px_1.load()
lst_grad_kirsh = []
max_bright = 0
min_bright = 1000
lst_mask_kirsh = [[ 3,  3,  3],
                  [ 3,  0,  3],
                  [-5, -5, -5]]
for i in range(px.size[0]):
    lst_grad_kirsh.append([])
    for j in range(px.size[1]):
        pixel = 0
        for mask_i in range(len(lst_mask_kirsh)):
            for mask_j in range(len(lst_mask_kirsh[mask_i])):
                try:
                    pixel -= px1[i - floor(len(lst_mask_kirsh)/2) + mask_i, j - floor(len(lst_mask_kirsh[mask_i])/2) + mask_j]*lst_mask_kirsh[mask_i][mask_j]
                except IndexError:
                    pixel -= px1[i, j]*lst_mask_kirsh[mask_i][mask_j]
        if max_bright < abs(pixel):
            max_bright = abs(pixel)
        if min_bright > abs(pixel):
            min_bright = abs(pixel)
        lst_grad_kirsh[i].append(abs(pixel))
        # if abs(pixel) > 250:
        #     px1[i, j] = (255)
        # else:
        #     px1[i, j] = (0)
#print(max_bright)
for i in range(px.size[0]):
    for j in range(px.size[1]):
        if lst_grad_kirsh[i][j] > max_bright*0.1:
            px1[i, j] = (255)
        else:
            px1[i, j] = (0)

# max_bright = max(lst_obj_kirish)*0.8
# for i in range(px.size[0]):
#     for j in range(px.size[1]):
#         if lst_obj_kirish[i*px.size[0] + j] > max_bright:
#             px1[i, j] = (255)
#         else:
#             px1[i, j] = (0)
px_1.save("./image_kirsh.jpg")