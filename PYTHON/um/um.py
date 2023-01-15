import re


def main():
    print(count(input("Text: ")))


def count(s):
    s_list = re.findall(r"um", s, re.IGNORECASE)

    return len(s_list)


if __name__ == "__main__":
    main()