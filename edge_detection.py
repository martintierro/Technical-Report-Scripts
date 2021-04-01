import cv2 as cv
import numpy as np
import csv

def edge_detection(filename, video_name):
    cap = cv.VideoCapture(filename)
    if (cap.isOpened() == False):
        print('Error while trying to read frames. Please check again...')
        
    # get the frame width and height
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    vid_codec = cv.VideoWriter_fourcc(*'mp4v')

    # define codec and create VideoWriter object
    out = cv.VideoWriter(f"edges/"+video_name+"(Edge).mp4", vid_codec, 30, (frame_width, frame_height))
    scale = 1
    delta = 0
    ddepth = cv.CV_16S

    # open csv file
    with open("Edge Count/" + video_name +" Edge Tally.csv", mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter = ',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["Frame Number", "Non-Zero Edge Count"])
        print("Detecting Edges")
        frame_count = 0
        # read until end of video
        total_edge_count = 0
        while(cap.isOpened()):
            # capture each frame of the video
            ret, frame = cap.read()
            if ret == True:
                # frame = cv.Laplacian(src=frame, ddepth=cv.CV_8U, ksize=3)
                src = cv.GaussianBlur(frame, (3, 3), 0)
                gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
                
                
                grad_x = cv.Sobel(gray, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
                grad_y = cv.Sobel(gray, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
                
                
                abs_grad_x = cv.convertScaleAbs(grad_x)
                abs_grad_y = cv.convertScaleAbs(grad_y)
                
                
                grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
                nzCount = cv.countNonZero(grad)
                csv_writer.writerow([frame_count, nzCount])
                frame_count = frame_count + 1
                total_edge_count = total_edge_count + nzCount

                # save video frame
                out.write(grad)
                # display frame
                cv.imshow('Video', grad)
                # press `q` to exit
                if cv.waitKey(27) & 0xFF == ord('q'):
                    break
            else:
                break
        csv_writer.writerow(["TOTAL", total_edge_count])
        average_edge_count = total_edge_count / (frame_count + 1)
        csv_writer.writerow(["AVERAGE", average_edge_count])
        print("Finished")
    # release VideoCapture()
    cap.release()
    # close all frames and video windows
    cv.destroyAllWindows()