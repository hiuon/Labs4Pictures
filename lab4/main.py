from PIL  import Image
from math import *

#import picture1 and convert it to L mode (only one component)
img      = Image.open("./image.jpg")
img_data = img.convert("L").getdata()

lst_mask = [1, 1, 1,
            1, 1, 1,
            1, 1, 1]
