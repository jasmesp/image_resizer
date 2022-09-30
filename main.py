import os
import time
from PIL import Image

#get out gooey package
def make_thumbnail_dir():
    root_output_dir = './imgs_out'
    make_thumbnail_dir = '/thumbnail'
    os.mkdir(root_output_dir + make_thumbnail_dir + '/')
    return root_output_dir + make_thumbnail_dir + '/'


imgs_dir = './imgs'
imgs_out_dir = make_thumbnail_dir()


# os.listdir(imgs_dir)

for file in os.listdir(imgs_dir):
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".JPG"):
        img = Image.open(imgs_dir + '/' + file)
        output_width = 300
        width_percentage = (output_width / float(img.size[0]))
        output_height = int((float(img.size[1]) * float(width_percentage)))
        img = img.resize((output_width, output_height))
        img.save(imgs_out_dir + 'thumb_' + file)
        print(file)
    else:
        print("Not a jpg")
        continue
