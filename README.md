# Resizr.py

Resizr is a basic implementation of the Pillow Python library. It provides a command line tool to resize pictures, taking user input for filename, and desired width/height(in pixels) of the resized image.

## Examples:

- Resize the file 'picture.jpg' to the standard 16:10 24 inch monitor resolution:
```./resizr.py -f picture.jpg -w 1920 -h 1200```

- Resize the file 'clowns.png' to a square image:
```./resizr.py -f clowns.png -w 500 -h 500```

## Release notes

- **v1.0.0** - Initial functional release
