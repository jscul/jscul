from pathlib import Path

import cv2

vids = []

for path in Path(".").rglob("*.mp4"):
    vids.append(path.absolute())
    f = cv2.VideoCapture(str(path.absolute()))
    rval, frame = f.read()
    img_path = f"{path.parent}/{path.name.replace('.mp4', '')}.png"
    print(img_path)
    cv2.imwrite(img_path, frame)
    f.release()
