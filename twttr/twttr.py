# program to remove vowels with input

# input to user
txt = input("Input: ")

# letters to remove
vowel = "aeiouAEIOU"

# add to place of removed letter
txt2 = ""

# create condition
for c in txt:
    if c not in vowel:
        txt2 = txt2 + c

# print result
print("Output:", txt2)
