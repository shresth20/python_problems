#food watch progarm
def main():
    ans = input("What time is it? ")
    time = convert(ans)
#create condition statement
    if 7 <= time <= 8:
        print("breakfast time")

    if 12 <= time <= 13:
        print("lunch time")

    if 18 <= time <= 19:
        print("dinner time")
#create fun.. to convert into float
def convert(time):
    houre,minutes = time.split(":")
    new_minutes = float(minutes ) / 60
    return float(houre) +  new_minutes

#call fun..
if __name__ == "__main__":
    main()