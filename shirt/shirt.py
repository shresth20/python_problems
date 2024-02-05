#import ower packages
import sys
from os.path import splitext
from PIL import Image, ImageOps

#get the command with conditions

file1 = splitext(sys.argv[1])
file2 = splitext(sys.argv[2])

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if file1[1] not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid input")
if file2[1] not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid output")
if file1[1].lower() != file2[1].lower():
    sys.exit("Input and output have different extensions")

#open the file with condition
try:
    img = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist")

#get the virtual shirt
shirt = Image.open("shirt.png")

#set size of shirt
size = shirt.size

#resize the virtual shirt
demo = ImageOps.fit(img, size)

#past virtual shirt
demo.paste(shirt, shirt)

#save ower image
demo.save(sys.argv[2])
