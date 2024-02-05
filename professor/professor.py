#import random packge
import random

#fun.. to call the fun..
def main():
    generate_integer(get_level())

#fun.. to get level value with user
def get_level():
    while True:
            try:
                lvl = int(input("Level: "))
                if lvl == 1:
                    level = 1
                    break
                elif lvl == 2:
                    level = 2
                    break
                elif lvl == 3:
                    level = 3
                    break
                else:
                    continue
            except ValueError:
                pass
    return level

#fun.. to get level value and create x & y value and check input !!
def generate_integer(level):
    s = 0
    i = 10
    while i != 0:
            if level == 1:
                x = random.randint(0,9)
                y = random.randint(0,9)

            elif level == 2:
                x = random.randint(10,99)
                y = random.randint(10,99)

            elif level == 3:
                x = random.randint(100,999)
                y = random.randint(100,999)

            e = 3
            while e != 0:
                try:
                    ans = int(input(f"{x} + {y} = "))
                    if ans == int(x + y):
                        s += 1
                        break
                    else:
                        print("EEE")
                except ValueError:
                    print("EEE")
                    pass
                if e == 1:
                    print(f"{x} + {y} = {x+y}")
                e -= 1
            i -= 1 #while 1

    print("score = ",s)


#call the fun.. with condition
if __name__ == "__main__":
    main()



