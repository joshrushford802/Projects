total = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

total_amt = 0

while True:
    try:
        inp = input("Item: ")
        inp = inp.lower()

        if inp in total:
            total_amt = total_amt + total[inp]
        else:
            pass
    except KeyError:
        pass
    except EOFError:
        break

    print(f"Total: ${total_amt:.2f}")