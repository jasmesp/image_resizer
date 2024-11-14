import os
from pathlib import Path

from PIL import Image


def make_thumbnail_dir():
    root_output_dir = Path("./imgs_out/")
    thumbnail_dir = root_output_dir / "thumbnail"

    root_output_dir.mkdir(exist_ok=True)
    thumbnail_dir.mkdir(exist_ok=True)
    return thumbnail_dir


def homogenize_filenames():
    imgs_dir = Path("./imgs")

    for file in imgs_dir.iterdir():
        if file.suffix.upper() in [".JPG", ".JPEG", ".PNG"]:
            file.rename(file.with_suffix(file.suffix.lower()))


imgs_dir = Path("./imgs")
imgs_out_dir = make_thumbnail_dir()

# os.listdir(imgs_dir)
homogenize_filenames()
for file in imgs_dir.iterdir():
    if file.suffix.lower() in [".jpg", ".jpeg", ".png"]:
        img = Image.open(file)
        output_width = 300
        width_percentage = output_width / float(img.size[0])
        output_height = int((float(img.size[1]) * float(width_percentage)))
        img = img.resize((output_width, output_height))
        output_path = imgs_out_dir / f"thumb_{file.name.lower()}"
        img.save(output_path)
        print(file.name)
    else:
        print("Not a jpg")
        continue
