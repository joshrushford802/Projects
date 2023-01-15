def main():
    voweless = shorten(input("Input: "))
    print(voweless)


def shorten(word):

    if word[1:].islower():
        output = word.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')
    else:
        output = word.replace('A', '').replace('E', '').replace('I', '').replace('O', '').replace('U', '')
    prt = print(output)
    return prt


if __name__ == "__main__":
    main()