import os
import pathlib

print("Run this from the directory that you want to convert image files for")

p = pathlib.Path(".")

target_suffix = ".avif"
image_exts = [
    ".jpg",
    ".JPG",
    ".jpeg",
    ".png",
]

for f in p.rglob("*"):
    if os.path.isfile(f):
        if f.suffix in image_exts:
            new_path = f.with_suffix(target_suffix)
            print(new_path)
            os.system(f"convert {f} -resize 1024\> {new_path}")
