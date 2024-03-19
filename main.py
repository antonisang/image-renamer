import os
import pathlib
from PIL import Image

path = input("Enter path to rename images (if none, the local dir will be used): ")
prefix = input("Enter prefix to rename images (if none, images will only contain their resolution in their name): ")
norm_path = pathlib.Path(path).resolve()

if not os.path.isdir(norm_path):
    print("Invalid path, please specify a valid path")
    exit(1)

images = list()

for extension in ["jpg", "jpeg", "png"]:
    images.extend(norm_path.glob(f"*.{extension}"))

if len(images) == 0:
    print("No images found")
    exit(1)

if prefix:
    prefix += " - "

for image in images:
    with Image.open(image, mode="r") as im:
        width, height = im.size
    os.rename(image, image.parent.joinpath(f"{prefix}{width} x {height}{image.suffix}"))
