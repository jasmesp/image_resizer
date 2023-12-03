import os

from PIL import Image


def make_thumbnail_dir():
    root_output_dir = "./imgs_out/"
    thumbnail_dir = "/thumbnail"
    thumbnail_path = root_output_dir + thumbnail_dir + "/"

    try:
        if not os.path.exists(root_output_dir):
            os.mkdir(root_output_dir)

        os.mkdir(thumbnail_path)
    except FileExistsError:
        pass

    return thumbnail_path


def homogenize_filenames():
    import os

    imgs_dir = "./imgs"

    for file in os.listdir(imgs_dir):
        if file.upper().endswith((".JPG", ".JPEG", ".PNG")):
            os.rename(
                os.path.join(imgs_dir, file), os.path.join(imgs_dir, file.lower())
            )


imgs_dir = "./imgs"
imgs_out_dir = make_thumbnail_dir()

# os.listdir(imgs_dir)
homogenize_filenames()
for file in os.listdir(imgs_dir):
    if file.lower().endswith((".jpg", ".jpeg", ".png")):
        img = Image.open(imgs_dir + "/" + file)
        output_width = 300
        width_percentage = output_width / float(img.size[0])
        output_height = int((float(img.size[1]) * float(width_percentage)))
        img = img.resize((output_width, output_height))
        img.save(imgs_out_dir + "thumb_" + file.lower())
        print(file)
    else:
        print("Not a jpg")
        continue
