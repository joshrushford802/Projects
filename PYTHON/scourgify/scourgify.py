import sys
import csv


if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif ".csv" not in sys.argv[2] and ".csv" not in sys.argv[1]:
    sys.exit("Not a CSV file")

first_csv_file = sys.argv[1]
second_csv_file = sys.argv[2]
out_file = []

try:
    with open(first_csv_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            breakup = row['name'].split(',')
            out_file.append({"first": breakup[1].lstrip(), "last": breakup[0], "house": row["house"]})
except FileNotFoundError:
    sys.exit(f"Could not read {first_csv_file}")

with open(second_csv_file, "w") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    writer.writerow({"first": "First", "last": "Last", "house": "House"})
    for row in out_file:
        writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})