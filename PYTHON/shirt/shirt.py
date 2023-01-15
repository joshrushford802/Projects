from PIL import Image, ImageOps
import sys


if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if ".jpg" not in sys.argv[1] or ".jpg" not in sys.argv[2]:
    sys.exit("Not a JPG file")
elif ".jpg" not in sys.argv[1] and ".jpg" in sys.argv[2]:
    sys.exit("Input and output have different extensions")
elif ".jpg" not in sys.argv[2] and ".jpg" in sys.argv[1]:
    sys.exit("Input and output have different extensions")

try:
    img = Image.open((sys.argv[1]))
except FileNotFoundError:
    sys.exit("Input does not exist")

shirt = Image.open("shirt.png")

size = shirt.size

pup = ImageOps.fit(img, size)

pup.paste(shirt, shirt)

pup.save(sys.argv[2])