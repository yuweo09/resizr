 #!bin/python

#filename: resizr.py

#import statements
import argparse
from PIL import Image
from resizeimage import resizeimage

#accept arguments at the command line with argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", "filename", type=str, help="Filename for image to be resized")
parser.add_argument("-w", "width", type=int, help="Desired width in pixels of new image")
parser.add_argument("-h", "height", type=int, help="Desired height in pixels of new image")
args = parser.parse_args()
with open(args.filename, 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [1920, 1200])
        cover.save('test.jpg', image.format)
