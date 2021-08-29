import cv2
import numpy as np


def to_frames(video_path, dir_path, start_at=0, end_at=None):
    vidcap = cv2.VideoCapture(video_path)

    success, image = vidcap.read()
    fno = 0
    while success and fno < end_at:
        cv2.imwrite(f"{dir_path}/{fno}.png", image)
        fno += 1


if __name__ == "__main__":
    to_frames("./JSC_4754.MOV", "./images", end_at=1)
