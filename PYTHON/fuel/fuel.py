while True:
    try:
        inp = input("Fraction: ")
        integer = inp.split("/")
        compute = int(integer[0]) / int(integer[1]) * 100
        compute = round(compute)

        if compute <= 1:
            print("E")
            break
        elif compute == 99 or compute == 100:
            print("F")
            break
        elif compute < 0 or compute > 100:
            pass
        else:
            print(f"{compute}%")
            break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass