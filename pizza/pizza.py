#import all requried packages
import sys
import csv
from tabulate import tabulate

#condiditon for commad !!
try:
    filee = sys.argv[1]

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if filee.endswith(".csv") == False:
        sys.exit("Not a CSV file")

except IndexError:
    sys.exit("Too few command-line arguments")

#conditions and print csv file into ascii form !!
try:
    with open(filee, "r") as file:
        lists = csv.reader(file)
        table = []
        for line in lists:
            table.append(line)
        print(tabulate(table, headers="firstrow", tablefmt="grid")) #print result !!

except FileNotFoundError:
    sys.exit("File does not exist")

