#import requered packges
import requests
import json
import sys

#get value from user using CLA with condition
try:
    n = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)
except IndexError:
    print("Missing command-line argument")
    sys.exit(1)

#fectching data from http link using json
responce = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
link = responce.json()

#get coin rate from data
js = link["bpi"]["USD"]["rate"]

#print result..
c = (js).replace(',', '')
rate = float(c)
amount = (rate * n)

print(f"${amount:,.4f}")
