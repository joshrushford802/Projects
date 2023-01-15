import cs50

print("Amount Due: 50")

amount_due = 50

while amount_due > 0:
    coin = int(input("Insert Coin: "))
    amount_due = amount_due - coin
    if amount_due < 0:
        print("Change Owed: ", abs(amount_due))
    else:
        print("Amount Due: ", amount_due)
    while coin != 25 and coin != 10 and coin != 5:
        coin = int(input("Insert Coin: "))
        amount_due = amount_due - coin
        if amount_due < 0:
            print("Change Owed: ", abs(amount_due))
        else:
            print("Amount Due: ", amount_due)