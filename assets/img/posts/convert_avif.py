import os
import pathlib

print("Run this from the directory that you want to convert image files for")

p = pathlib.Path(".")

# iterate over files in
# that directory
for f in p.rglob("*"):
    # f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)

