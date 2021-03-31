import cv2 as cv
from matplotlib import pyplot as plt
import os
import PIL
from PIL import Image
from os.path import isfile, join
import numpy as np

def get_hsv(folderpath):
    imlist = [f for f in os.listdir(folderpath) if isfile(join(folderpath, f))]
    
    # Assuming all images are the same size, get dimensions of first image
    w,h=Image.open(folderpath + "/" + imlist[0]).size
    N=len(imlist)

    # Create a numpy array of floats to store the average (assume RGB images)
    arr=np.zeros((h,w,3),np.float)

    # Build up average pixel intensities, casting each image as an array of floats
    print("Computing for HSV")
    for im in imlist:
        imarr=np.array(Image.open(folderpath+"/"+im),dtype=np.float)
        arr=arr+imarr/N

    # Round values in array and cast as 8-bit integer
    arr=np.array(np.round(arr),dtype=np.uint8)

    # Generate, save and preview final image
    avg=Image.fromarray(arr,mode="RGB")
    avg.save(folderpath + "/Average.png")
    avg.show()

    avg_img = cv.imread(folderpath+"/Average.png")
    avg_hsv = cv.cvtColor(avg_img,cv.COLOR_BGR2HSV)
    hist = cv.calcHist( [avg_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256] )
    plt.imshow(hist,interpolation = 'nearest')
    plt.show()
    print("Finished")
