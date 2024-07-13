import os
import pathlib

p = pathlib.Path(".")

target_suffix = ".webp"
image_exts = [
    ".jpg",
    ".JPG",
    ".jpeg",
    ".png",
]

for f in p.rglob("*"):
    if os.path.isfile(f) and f.suffix in image_exts:
        new_path = f.with_suffix(target_suffix)
        if not new_path.exists():  # Check if the webp file does not already exist
            print(f"Converting {f} to {new_path}")
            os.system(f"convert {f} -resize 1024\> {new_path}")

# To convert from gif to webp:
# ffmpeg -i input.gif -vcodec webp -loop 0 -pix_fmt yuva420p output.webp
