import numpy as np
import matplotlib.pyplot as plt
import argparse
import cv2 as cv
import PIL
import io
import os

def get_realtime_color_histogram(filename, video_name):
    capture = cv.VideoCapture(filename)
    
    # get the frame width and height
    frame_width = 640
    frame_height = 480
    vid_codec = cv.VideoWriter_fourcc(*'mp4v')
    fps = capture.get(cv.CAP_PROP_FPS)
    
    color = 'rgb'
    bins = 16
    resizeWidth = 0
    
    # Initialize plot.
    fig, ax = plt.subplots()
    if color == 'rgb':
        ax.set_title('Histogram (RGB)')
    else:
        ax.set_title('Histogram (grayscale)')
    ax.set_xlabel('Bin')
    ax.set_ylabel('Frequency')

    # Initialize plot line object(s). Turn on interactive plotting and show plot.
    lw = 3
    alpha = 0.5
    if color == 'rgb':
        lineR, = ax.plot(np.arange(bins), np.zeros((bins,)), c='r', lw=lw, alpha=alpha)
        lineG, = ax.plot(np.arange(bins), np.zeros((bins,)), c='g', lw=lw, alpha=alpha)
        lineB, = ax.plot(np.arange(bins), np.zeros((bins,)), c='b', lw=lw, alpha=alpha)
    else:
        lineGray, = ax.plot(np.arange(bins), np.zeros((bins,1)), c='k', lw=lw)
    ax.set_xlim(0, bins-1)
    # ax.set_ylim(0, 1)
    plt.ion()
    plt.show()

    out = cv.VideoWriter(f"HSV Videos/"+video_name+" - HSV.mp4", vid_codec, fps, (frame_width, frame_height))

    # Grab, process, and display video frames. Update plot line object(s).
    run_flag = True
    while True:
        (grabbed, frame) = capture.read()

        if not grabbed:
            break

        # Resize frame to width, if specified.
        if resizeWidth > 0:
            (height, width) = frame.shape[:2]
            resizeHeight = int(float(resizeWidth / width) * height)
            frame = cv.resize(frame, (resizeWidth, resizeHeight),
                interpolation=cv.INTER_AREA)
        # Normalize histograms based on number of pixels per frame.
        numPixels = np.prod(frame.shape[:2])
        if color == 'rgb':
            cv.imshow('RGB', frame)
            (b, g, r) = cv.split(frame)
            histogramR = cv.calcHist([r], [0], None, [bins], [0, 255]) / numPixels
            histogramG = cv.calcHist([g], [0], None, [bins], [0, 255]) / numPixels
            histogramB = cv.calcHist([b], [0], None, [bins], [0, 255]) / numPixels
            lineR.set_ydata(histogramR)
            lineG.set_ydata(histogramG)
            lineB.set_ydata(histogramB)
            maxR = max(histogramR)
            maxG = max(histogramG)
            maxB = max(histogramB)
        else:
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            cv.imshow('Grayscale', gray)
            histogram = cv.calcHist([gray], [0], None, [bins], [0, 255]) / numPixels
            lineGray.set_ydata(histogram)
        maxY = max(maxR, maxG, maxB)

        if(run_flag):
            ax.set_ylim(0, maxY + 0.025)
            run_flag = False

        fig.canvas.draw()
        fig.savefig("HSV Videos/" + video_name + " temp.png")

        hist_frame  = cv.imread("HSV Videos/" + video_name + " temp.png")
        out.write(hist_frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    
    os.remove("HSV Videos/" + video_name + " temp.png")
    capture.release()
    cv.destroyAllWindows()
    out.release()
