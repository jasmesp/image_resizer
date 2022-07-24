import PIL
import os
from PIL import Image

imgs_dir = './imgs'
imgs_out_dir = './imgs_out'

os.listdir(imgs_dir)

for file in os.listdir(imgs_dir):
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".JPG"):
        img = Image.open(imgs_dir + '/' + file)
        output_width = 300
        width_percentage = (output_width / float(img.size[0]))
        output_height = int((float(img.size[1]) * float(width_percentage)))
        img = img.resize((output_width, output_height))
        img.save(imgs_out_dir + '/' + file)
        print(file)
    else:
        print("Not a jpg")
        continue
