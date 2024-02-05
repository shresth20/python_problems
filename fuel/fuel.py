#create fun... to Fuel Gauge
def main():
    while True:
        try:
            value = input("Fraction: ")
            x, y = value.split("/")
            new_x = int(x)
            new_y = int(y)
            c = new_x/new_y
            if c <= 1:
                break
        except (ValueError, ZeroDivisionError, ):
            pass
    fuel = round(c*100)
    if fuel <= 1:
        print("E")
    elif fuel >= 99:
        print("F")
    else:
        print(fuel,"%", sep="")

#call the fun..
main()













