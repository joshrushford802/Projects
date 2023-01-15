import tabulate
import sys
import csv


if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif ".csv" not in sys.argv[1]:
    sys.exit("Not a CSV file")

csv_file = sys.argv[1]
table = []

try:
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            table.append(row)
except FileNotFoundError:
    sys.exit("File does not exist")

print(tabulate.tabulate(table[1:], headers=table[0], tablefmt='grid'))