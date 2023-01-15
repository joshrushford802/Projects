from pyfiglet import Figlet
import sys
import random


figlet = Figlet()

if len(sys.argv) == 1:
    figlet.setFont(font=(random.choice(figlet.getFonts())))
elif (len(sys.argv) == 3) and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    figlet.setFont(font=sys.argv[2])
else:
    print("Incorrect arguments")
    sys.exit(1)

inp = input("Input: ")

print(figlet.renderText(inp))