import sys


if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif ".py" not in sys.argv[1]:
    sys.exit("Not a Python file")

py_file = sys.argv[1]
counter = 0

try:
    with open(py_file) as file:
        for line in file:
            if ("#" in line) or (line.startswith("\n") and line.endswith("\n")):
                pass
            else:
                counter += 1
        print(counter)
except FileNotFoundError:
    sys.exit("File does not exist")