#import command line arg.. package
import sys

#false commands comments
try:
    filee = sys.argv[1]

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if filee.endswith(".py") == False:
        sys.exit("Not a Python file")

except IndexError:
    sys.exit("Too few command-line arguments")

#fun.. for check line blanklines and # lines
def false_line(line):
    if line.isspace():
        return True
    if line.lstrip().startswith("#"):
        return True
    return False

#count the lines with conditions
try:
    with open(filee, "r") as file:
        lines = file.readlines()

    total_line = 0
    for line in lines:
        if false_line(line) == False:
            total_line += 1
    print(total_line)       #print total codes lines

except FileNotFoundError:
    sys.exit("File does not exist")

