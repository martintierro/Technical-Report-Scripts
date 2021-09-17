import cv2 as cv
import os
from tkinter import Tk # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

def convert_to_png(filename, folderpath):
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

    if not os.path.exists("E:\\Projects\\Thesis\\Baseline B\\SOF-VSR\\TIP\\data\\test\\Others\\" + folderpath):
        os.makedirs("E:\\Projects\\Thesis\\Baseline B\\SOF-VSR\\TIP\\data\\test\\Others\\" + folderpath)
    if not os.path.exists("E:\\Projects\\Thesis\\Baseline B\\SOF-VSR\\TIP\\data\\test\\Others\\" + folderpath + "\\hr"):
        os.makedirs("E:\\Projects\\Thesis\\Baseline B\\SOF-VSR\\TIP\\data\\test\\Others\\" + folderpath+ "\\hr")


    print("Currently converting video to frames")
    while True:
        ret, frame = capture.read()
        if frame is None:
            break
        
        # cv.imwrite(folderpath +"/Frame " + str(frame_counter) +'.png',frame)
        cv.imwrite("E:\\Projects\\Thesis\\Baseline B\\SOF-VSR\\TIP\\data\\test\\Others\\" + folderpath + "\\hr\\hr_" + str(frame_counter) +'.png',frame)
        frame_counter = frame_counter + 1
        
        keyboard = cv.waitKey(30)
        if keyboard == 'q' or keyboard == 27:
            break
    print("Finished")

    # When everything done, release the video capture and video write objects
    capture.release()
    
    # Closes all the frames
    cv.destroyAllWindows() 

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

temp = filename.split("/")
fn = temp[-1]
newdir = fn.split(".")

convert_to_png(filename, newdir[0])