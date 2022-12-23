import os
from PIL import Image, ImageEnhance, ImageFilter


path = "./imgs"  # dir for unedited images.
pathOut = "./editedImgs"  # dir for edited images.

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    # sharpening, Black&White
    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)

    # contrast
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    # renaming edited photos.
    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')
