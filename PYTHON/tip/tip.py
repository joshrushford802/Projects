import cs50

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dd = d.replace('$', '')
    return float(dd)


def percent_to_float(p):
    pp = p.replace('%', '')
    ppp = float(pp) / 100
    return ppp


main()