import sys
import csv
try:
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if file1.endswith(".csv") == False:
        sys.exit("Not a csv file")
    if file2.endswith(".csv") == False:
        sys.exit("Not a csv file")

except IndexError:
    sys.exit("Too few command-line arguments")


try:
    newlist = []
    with open(file1, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row["name"].split(",")
            newlist.append({"first": name[1].lstrip(), "last": name[0].lstrip(), "house": row["house"]})

    with open(file2, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for row in newlist:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})

except FileNotFoundError:
    sys.exit(f"Could not read {file1}")


