import cv2 as cv
import os

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

    if not os.path.exists("D:\\Projects\\Thesis\\Baseline B\\SOF-VSR\\TIP\\data\\test\\Set\\" + folderpath):
        os.makedirs("D:\\Projects\\Thesis\\Baseline B\\SOF-VSR\\TIP\\data\\test\\Set\\" + folderpath)
    if not os.path.exists("D:\\Projects\\Thesis\\Baseline B\\SOF-VSR\\TIP\\data\\test\\Set\\" + folderpath + "\\hr"):
        os.makedirs("D:\\Projects\\Thesis\\Baseline B\\SOF-VSR\\TIP\\data\\test\\Set\\" + folderpath+ "\\hr")


    print("Currently converting video to frames")
    while True:
        ret, frame = capture.read()
        if frame is None:
            break
        
        # cv.imwrite(folderpath +"/Frame " + str(frame_counter) +'.png',frame)
        cv.imwrite("D:\\Projects\\Thesis\\Baseline B\\SOF-VSR\\TIP\\data\\test\\Set\\" + folderpath + "\\hr\\hr_" + str(frame_counter) +'.png',frame)
        frame_counter = frame_counter + 1
        
        keyboard = cv.waitKey(30)
        if keyboard == 'q' or keyboard == 27:
            break
    print("Finished")

    # When everything done, release the video capture and video write objects
    capture.release()
    
    # Closes all the frames
    cv.destroyAllWindows() 