# This checks for the correct user input.
while True:
    try:
        symbol = int(input("Height: "))
        if symbol > 0 and symbol < 9:
            break
    except ValueError:
        print("Incorrect")

# This iterates over each row, adding hashes and spaces depending on what the user entered for input.
for r in range(0, symbol, 1):
    for k in range(0, symbol, 1):
        if(r+k < symbol-1):
            print(" ", end="")
        else:
            print("#", end="")
    print()