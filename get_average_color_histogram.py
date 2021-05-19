import cv2 as cv
from matplotlib import pyplot as plt
import os
import PIL
from PIL import Image
from os.path import isfile, join
import numpy as np

def get_average_color_histogram(video_name):
    imlist = [f for f in os.listdir("Frames/"+video_name) if isfile(join("Frames/"+video_name, f))]
    
    # Assuming all images are the same size, get dimensions of first image
    w,h=Image.open("Frames/"+video_name + "/" + imlist[0]).size
    N=len(imlist)

    # Create a numpy array of floats to store the average (assume RGB images)
    arr=np.zeros((h,w,3),np.float)

    # Build up average pixel intensities, casting each image as an array of floats
    print("Computing for HSV")
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.set_title(video_name + "\nHSV 3D Scatter Plot")
    ax.set_xlabel("Frame Number")
    ax.set_ylabel("Hue")
    ax.set_zlabel("Saturation")
    x = 1
    for im in imlist:
        imarr=np.array(Image.open("Frames/"+video_name+"/"+im),dtype=np.float)
        arr=arr+imarr/N

        img = cv.imread("Frames/"+video_name+"/"+im)
        hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
        h, s, v = cv.split(hsv)
        y = np.average(h)
        z = np.average(s)
        ax.scatter(x, y, z)
        x = x + 1
    
    # plt.show()
    fig.savefig("HSV/"+ video_name +" - Scatter Plot.png")


    # Round values in array and cast as 8-bit integer
    arr=np.array(np.round(arr),dtype=np.uint8)

    # Generate, save and preview final image
    avg=Image.fromarray(arr,mode="RGB")
    avg.save("Frames/"+ video_name + "/Average.png")
    # avg.show()
    
    #HSV Plot
    # fig, ax = plt.subplots()

    # avg_hsv = cv.cvtColor(avg_img,cv.COLOR_BGR2HSV)
    # ax.scatter3D(h, s, v, color = "green")
    # # hist = cv.calcHist( [avg_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256] )

    # plt.show()
    # fig.savefig("HSV/"+ video_name +" - Scatter Plot.png")
    bins = 16
    lw = 3
    alpha = 0.5
    
    avg_img = cv.imread("Frames/"+video_name+"/Average.png")
    #RGB Graph
    fig, ax = plt.subplots()
    ax.set_title(video_name + "\nColor Histogram Plot")
    ax.set_xlabel("Bins")
    ax.set_ylabel("Frequency")
    # for i, col in enumerate(['b', 'g', 'r']):
    #     hist = cv.calcHist([avg_img], [i], None, [256], [0, 256])
    #     plt.plot(hist, color = col)
    #     plt.xlim([0, 256])
    lineR, = ax.plot(np.arange(bins), np.zeros((bins,)), c='r', lw=lw, alpha=alpha)
    lineG, = ax.plot(np.arange(bins), np.zeros((bins,)), c='g', lw=lw, alpha=alpha)
    lineB, = ax.plot(np.arange(bins), np.zeros((bins,)), c='b', lw=lw, alpha=alpha)
    numPixels = np.prod(avg_img.shape[:2])

    (b, g, r) = cv.split(avg_img)
    histogramR = cv.calcHist([r], [0], None, [bins], [0, 255]) / numPixels
    histogramG = cv.calcHist([g], [0], None, [bins], [0, 255]) / numPixels
    histogramB = cv.calcHist([b], [0], None, [bins], [0, 255]) / numPixels
    lineR.set_ydata(histogramR)
    lineG.set_ydata(histogramG)
    lineB.set_ydata(histogramB)
    maxR = max(histogramR)
    maxG = max(histogramG)
    maxB = max(histogramB)
    maxY = max(maxR, maxG, maxB)
    ax.set_ylim(0, maxY + 0.025)
    fig.canvas.draw()
    fig.savefig("HSV/"+ video_name +" - Histogram.png")

    # plt.close('all')
    print("Finished")
