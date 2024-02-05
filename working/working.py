import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    Format = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
    if Format:
        time = Format.groups()
        if 12 < int(time[1]) or int(time[5]) > 12:
            raise ValueError
        time1 = newf(time[1], time[2], time[3])
        time2 = newf(time[5], time[6], time[7])
        return time1 + ' to ' + time2
    else:
        raise ValueError


def newf(hour, min, am_pm):
    if am_pm == "PM":
        if int(hour) == 12:
            newh = 12
        else:
            newh = int(hour) + 12
    else:
        if int(hour) == 12:
            newh = 0
        else:
            newh = int(hour)

    if min == None:
        newm = ":00"
        newt = f"{newh:02}" + newm
    else:
        newt = f"{newh:02}" + ":" + min
    return newt


if __name__ == "__main__":
    main()