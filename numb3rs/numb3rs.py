import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search("^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):

        list = ip.split(".")
        for num in list:
            if 0 > int(num) or int(num) > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()