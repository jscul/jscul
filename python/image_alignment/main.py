from __future__ import print_function

import cv2
import numpy as np

MAX_FEATURES = 500
GOOD_MATCH_PERCENT = 0.1


def getFrame(file_name, frame_num):
    cap = cv2.VideoCapture(file_name)
    totalFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    # check for valid frame number
    if frame_num >= 0 & frame_num <= totalFrames:
        # set frame position
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)

    ret, frame = cap.read()

    if not ret:
        return None

    return frame


def alignImages(im1, im2, i=0):

    # Convert images to grayscale
    im1Gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    im2Gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

    # Detect ORB features and compute descriptors.
    orb = cv2.ORB_create(MAX_FEATURES)
    keypoints1, descriptors1 = orb.detectAndCompute(im1Gray, None)
    keypoints2, descriptors2 = orb.detectAndCompute(im2Gray, None)

    # Match features.
    matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
    matches = matcher.match(descriptors1, descriptors2, None)

    # Sort matches by score
    matches.sort(key=lambda x: x.distance, reverse=False)

    # Remove not so good matches
    numGoodMatches = int(len(matches) * GOOD_MATCH_PERCENT)
    matches = matches[:numGoodMatches]

    # Draw top matches
    imMatches = cv2.drawMatches(im1, keypoints1, im2, keypoints2, matches, None)
    # cv2.imwrite(f"matches_{i}.jpg", imMatches)

    # Extract location of good matches
    points1 = np.zeros((len(matches), 2), dtype=np.float32)
    points2 = np.zeros((len(matches), 2), dtype=np.float32)

    for i, match in enumerate(matches):
        points1[i, :] = keypoints1[match.queryIdx].pt
        points2[i, :] = keypoints2[match.trainIdx].pt

    # Find homography
    h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)

    # Use homography
    height, width, channels = im2.shape
    im2Reg = cv2.warpPerspective(im2, h, (width, height))

    return im2Reg, h


if __name__ == "__main__":

    vidcap = cv2.VideoCapture("./JSC_4754.MOV")
    out = cv2.VideoWriter("project.avi", cv2.VideoWriter_fourcc(*"DIVX"), 60, (1920, 1080))

    success, image = vidcap.read()
    fno = 0
    while success and fno < 20:
        out.write(image)
        cv2.imwrite(f"./images/{fno}.png", image)

        print(fno)
        next_success, next_image = vidcap.read()

        print("Aligning images ...")
        # Registered image will be resotred in imReg.
        # The estimated homography will be stored in h.
        imReg, h = alignImages(image, next_image, fno)

        # Write aligned image to disk.
        outFilename = f"aligned_{fno}.jpg"
        print("Outputting aligned image : ", outFilename)
        # cv2.imwrite(outFilename, imReg)

        # Print estimated homography
        # print("Estimated homography : \n", h)

        # update for next time (change to success, image if reverting)
        success, image = next_success, imReg

        fno += 1

    out.release()
