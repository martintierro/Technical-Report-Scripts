from tkinter import Tk # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from convert_to_png import convert_to_png
from get_realtime_color_histogram import get_realtime_color_histogram
from get_average_color_histogram import get_average_color_histogram
from edge_detection import edge_detection
import os

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

temp = filename.split("/")
fn = temp[-1]
newdir = fn.split(".")

if not os.path.exists("Frames"):
    os.makedirs("Frames")

if not os.path.exists("Frames/" + newdir[0]):
    os.makedirs("Frames/" + newdir[0])

if not os.path.exists("Edge Videos"):
    os.makedirs("Edge Videos")

if not os.path.exists("Edge Count"):
    os.makedirs("Edge Count")

if not os.path.exists("HSV"):
    os.makedirs("HSV")

if not os.path.exists("HSV Videos"):
    os.makedirs("HSV Videos")

# convert_to_png(filename, newdir[0])
# get_realtime_color_histogram(filename, newdir[0])
get_average_color_histogram(newdir[0])
# edge_detection(filename,newdir[0])