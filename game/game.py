#import radom packge
import random

#loop to check and input
while True:
    try:
        level = int(input("Level: "))
        if 0 < level < 100:
            break
    except ValueError:
        pass

#call random fun.. and get value
x = random.randint(1,level)

#loop to check and input
while True:
    try:
        guess = int(input("Guess: "))
        if 0 < guess < 100:
            if guess < x:
                print("Too small!")
            elif guess > x:
                print("Too large!")
            else:
                print("Just right!")
                break
    except ValueError:
        pass
