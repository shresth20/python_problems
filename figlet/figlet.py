import pyfiglet
from pyfiglet import Figlet
import sys

if len(sys.argv) <= 1:
    print(pyfiglet.figlet_format(input("Input: ")))
    sys.exit("Invalid usage")

elif len(sys.argv) > 1:
    if sys.argv[1] != str("-f") and sys.argv[1] != str("--font"):
        sys.exit("Invalid usage")
    if sys.argv[2] not in  Figlet().getFonts():
        sys.exit("Invalid usage")

txt = input("Input: ")
print("Output: \n", pyfiglet.figlet_format(txt, font=f'{sys.argv[2]}'))
