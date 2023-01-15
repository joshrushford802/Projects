def main():
    frac = convert(input("Fraction: "))
    print(gauge(frac))


def convert(fraction):
    integer = fraction.split("/")
    compute = int(integer[0]) / int(integer[1]) * 100
    compute = round(compute)
    if compute > 0 and compute <= 100:
        return compute
    elif compute > 100:
        raise ValueError("Number over 100")
    elif compute < 0:
        raise ZeroDivisionError("Number over 100")


def gauge(percentage):

    if percentage <= 1:
        return "E"
    elif percentage == 99 or percentage == 100:
        return "F"
    elif percentage > 1 and percentage < 99:
        temp = percentage
        return (f"{temp}%")


if __name__ == "__main__":
    main()