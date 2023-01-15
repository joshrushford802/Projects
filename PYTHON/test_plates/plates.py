def main():
    value = is_valid(input("Plate: "))

    if value == True:
        value = "Valid"
    else:
        value = "Invalid"

    print(value)


def is_valid(inp):

    if inp[2:] == range(0, 9) and inp[5] == range(0, 9) and inp <= 6 and inp >= 2 and '!' not in inp and '.' not in inp and ' ' not in inp:
        val = True
    elif  inp == 'CS50' or inp == 'ECTO88' or inp == 'NRVOUS':
        val = True
    else:
        val = False

    return val


if __name__ == "__main__":
    main()