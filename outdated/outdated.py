months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
        date = input("Date: ").strip(" ")
        if "/" in date:
            m, d, y = date.split("/")
        elif "," in date:
            date = date.replace(",", "")
            m, d, y = date.split(" ")
            if m in months:
                m = months.index(m) + 1
        try:
            if int(m) > 12 or int(d) > 31:
                continue
            else:
                break
        except (ValueError,NameError):
             continue
print(y + "-" + f"{int(m):02}" + "-" + f"{int(d):02}", sep="", end=" ")



