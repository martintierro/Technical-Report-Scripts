from tkinter import Tk # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from convert_to_png import convert_to_png
from get_hsv import get_hsv
from edge_detection import edge_detection
import os

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

temp = filename.split("/")
fn = temp[-1]
newdir = fn.split(".")

if not os.path.exists(newdir[0]):
    os.makedirs(newdir[0])

if not os.path.exists("edges"):
    os.makedirs("edges")

convert_to_png(filename, newdir[0])
# get_hsv(newdir[0])
edge_detection(filename,newdir[0])