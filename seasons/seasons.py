# importing requered packages
from datetime import date
import sys
import re
import inflect


p = inflect.engine()

# number to word fun..
def main():
    birth = input("Date of Birth: ")
    try:
        year,month,day = check_birthday(birth)
    except:
        sys.exit("Invalid date")
    DOB = date(int(year), int(month), int(day))
    today = date.today()
    dif = today - DOB
    num_to_word = p.number_to_words(dif.days * 24 * 60, andword="")
    print(num_to_word.capitalize() + " minutes")


# function to check date of birth
def check_birthday(birth):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$",birth):
        year,month,date = birth.split("-")
        return year,month,date

# call the fun...
if __name__ == "__main__":
    main()