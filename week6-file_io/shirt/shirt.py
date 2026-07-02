# expects exactly two command-line arguments ✔
    # in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input ✔
    # in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output ✔

# The program should then overlay "shirt.png" on the input 
# after resizing and cropping the input to be the "same size"
# saving the result as its output

# The program should instead exit via "sys.exit": ✔
    # if the user does not specify exactly two command-line arguments, ✔
        # "Too few command-line arguments" ✔
        # "Too many command-line arguments" ✔
    # if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively, ✔
        # "Invalid output" ✔
        # "Invalid input" ✔
    # if the input’s name does not have the same extension as the output’s name ✔
        # "Input and output have different extensions" ✔
    # or if the specified input does not exist. ✔
        # "Input does not exist"

# ✅ python shirt.py before1.jpg after1.jpg 

from PIL import Image, ImageOps
import sys
import os


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    infilename = sys.argv[1]
    outfilename = sys.argv[2]
    validformat = (".jpg", ".jpeg", ".png")

    if not infilename.lower().endswith(validformat):
        sys.exit("Invalid input")
    if not outfilename.lower().endswith(validformat):
        sys.exit("Invalid output")

    # to check the formats
    in_root, in_ext = os.path.splitext(infilename)
    out_root, out_ext = os.path.splitext(outfilename)

    if in_ext.lower() != out_ext.lower():
        sys.exit("Input and output have different extensions")


    try:
        overlay_shirt(infilename, outfilename)
    except FileNotFoundError:
        sys.exit("Input does not exist")


def overlay_shirt(infilename, outfilename):
    with Image.open("shirt.png") as shirt, Image.open(infilename) as face:
        # 1) Find the size of shirt.png
        shirt_size = shirt.size # returns a tuple for size
    
        # 2) Resize and crop the input image (using default values for method, bleed, and centering)
        fitface = ImageOps.fit(face, shirt_size)
        
        # 3) Overlay the shirt on fitted face image
        # the second shirt represents a “mask” indicating which pixels in fitface to update.
        fitface.paste(shirt, shirt)

        # 4) Save the result as its output
        fitface.save(outfilename)


if __name__ == "__main__":
    main()