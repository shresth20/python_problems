#fun.. to input
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#fun..to define conditions of valid
def is_valid(s):
    #limitation and check first 2 letter
    if 6 >= len(s) >= 2 and s[0:2].isalpha() and s.isalnum():

    #loop to check "0" and alphabates
        for c in s:
            if c.isdigit():
                index = s.index(c)
                if s[index:].isdigit() and int(c) != 0:
                    return True
                else:
                    return False

    #pass ture when all conditions is true
        return True



#call the fun..
main()