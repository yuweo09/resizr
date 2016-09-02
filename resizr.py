#!bin/python

#filename: resizr.py

#import statements
import argparse
from PIL import Image
from resizeimage import resizeimage

#function to take filename, desired width/height, and create resized image
def imgresize(img, wt, ht):
    with open(img, 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [wt, ht])
            cover.save(img + '_resize_' + str(wt) + 'x' + str(ht) + '.jpg', image.format)

#if called directly
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-f", "--filename", required=True, type=str, help="Filename for image to be resized")
    parser.add_argument("-w", "--width", required=True, type=int, help="Desired width in pixels of new image")
    parser.add_argument("-h", "--height", required=True, type=int, help="Desired height in pixels of new image")
    args = parser.parse_args()

    imgresize(args.filename, args.width, args.height)
