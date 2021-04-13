import cv2 as cv

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

    print("Currently converting video to frames")
    while True:
        ret, frame = capture.read()
        if frame is None:
            break
        
        cv.imwrite("Frames/" + folderpath +"/Frame " + str(frame_counter) +'.png',frame)
        frame_counter = frame_counter + 1
        
        keyboard = cv.waitKey(30)
        if keyboard == 'q' or keyboard == 27:
            break
    print("Finished")

    # When everything done, release the video capture and video write objects
    capture.release()
    
    # Closes all the frames
    cv.destroyAllWindows() 