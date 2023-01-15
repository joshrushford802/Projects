def main():
    val = value(input("Greeting: "))
    print(f"${val}")


def value(greeting):
    greet = greeting.strip().lower()

    if 'hello' in greet:
        valu = 0
    elif greet[0] == 'h':
        valu = 20
    else:
        valu = 100

    return valu


if __name__ == "__main__":
    main()