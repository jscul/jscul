# https://github.com/Saafke/EDSR_Tensorflow/tree/master/models

import datetime

import cv2
from cv2 import dnn_superres

count = cv2.cuda.getCudaEnabledDeviceCount()
print(count)

# Create an SR object
sr = dnn_superres.DnnSuperResImpl_create()

# Read image
image = cv2.imread("./acozlzkz.png")

# Read the desired model
path = "EDSR_x4.pb"
sr.readModel(path)

# Set the desired model and scale to get correct pre- and post-processing
sr.setModel("edsr", 3)

# Upscale the image
a = datetime.datetime.now()
result = sr.upsample(image)
b = datetime.datetime.now()
c = b - a

print(c)

# Save the image
cv2.imwrite("./upscaled.png", result)
frames = "153342"
