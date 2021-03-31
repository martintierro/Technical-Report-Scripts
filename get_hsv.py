import cv2 as cv
from matplotlib import pyplot as plt
import os
from os.path import isfile, join
import numpy as np

def get_hsv(filename):
    # files = [f for f in os.listdir(folderpath) if isfile(join(folderpath, f))]
    # frame_count = len(files)
    # total = 0
    # images = []
    # for frame in files:
    #     img = cv.imread(folderpath + "/" + frame)
    #     images.append(img)
    #     hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

    capture = cv.VideoCapture()
    capture.open(filename)
    if not capture.isOpened():
        print('Unable to open')
        exit(0)
    #Get video dimensions
    frame_width = int(capture.get(3))
    frame_height = int(capture.get(4))
    fps = capture.get(cv.CAP_PROP_FPS)

    frame_counter = 0
    images = []

    while True:
        ret, frame = capture.read()
        if frame is None:
            break
        images.append(frame)
        keyboard = cv.waitKey(30)
        if keyboard == 'q' or keyboard == 27:
            break
    # cv.imshow("Image",img)
    # cv.imshow("HSV", hsv)
    avg_img = np.mean(images, axis=0)
    avg_hsv = cv.cvtColor(avg_img,cv.COLOR_BGR2HSV)
    cv.imshow("Average Image", avg_img)
    cv.imshow("Average HSV", avg_hsv)
    hist = cv.calcHist( [avg_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256] )
    plt.imshow(hist,interpolation = 'nearest')
    plt.show()
