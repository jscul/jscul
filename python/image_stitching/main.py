# Combine multiple images into one.
#
# pip install Pillow opencv-python
#
import os

import imutils
import cv2
import glob

from PIL import Image

is_vertical = True

for name in glob.glob("test/*"):

    print(f"Processing: {name}")

    if os.path.isdir(name):

        file_paths = glob.glob(f"{name}/*")
        images = []

        for image_path in file_paths:
            image = cv2.imread(image_path)
            if is_vertical:
                image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
            images.append(image)

        stitcher = cv2.createStitcher() if imutils.is_cv3() else cv2.Stitcher_create()
        (status, stitched) = stitcher.stitch(images)

        if status == 0:
            if is_vertical:
                stitched = cv2.rotate(stitched, cv2.ROTATE_90_COUNTERCLOCKWISE)
            cv2.imwrite(f"{name}.png", stitched)
        else:
            print(f"Image stitching failed ({status})")

    else:
        print("Files should be in subdirectory of test.")
