import cv2

cap = cv2.VideoCapture("your_name.mkv")
cap.set(1, 30000)

length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(length)

success, image = cap.read()
count = 0
success = True
while count < 1:
    success, image = cap.read()
    cv2.imwrite("frame%d.jpg" % count, image)  # save frame as JPEG file
    count += 1
