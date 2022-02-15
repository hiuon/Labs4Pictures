from PIL import Image

#constants
plus_value = -100
multiply_value = 2
r_neg = 100
r_log = 2

#lists of pixels
lst_plus = []
lst_multiply = []
lst_neg = []
lst_log = []

#import picture and convert it to L mode (only one component)
img = Image.open("./image.jpg")
img_data = img.convert("L").getdata()



for i in img_data:
    if i + plus_value > 255:
        lst_plus.append(255)
    elif i + plus_value < 0:
        lst_plus.append(0)
    else:
        lst_plus.append(i + plus_value)

img1 = Image.new("L", img.size)
img1.putdata(lst_plus)
img1.save("./image_new.jpg")