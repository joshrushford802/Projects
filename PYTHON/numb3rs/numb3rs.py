import re
import sys


def main():
    inp = input("IPv4 Address: ")

    print(validate(inp))



def validate(ip):
    if re.search("^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        split = ip.split(".")
        for _ in split:
            if int(_) > 255 or int(_) < 0:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()