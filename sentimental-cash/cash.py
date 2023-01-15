# Check for correct user input.
while True:
    try:
        cents = float(input("Change owed: "))
        if cents >= 0:
            break
        else:
            print("**Rejected**")
    except ValueError:
        print("**Rejected**")

quarters = 0
dimes = 0
nickels = 0
pennies = 0

# Calculate number of quarters.
while cents >= 0.25:
    cents = cents - 0.25
    quarters = quarters + 1

# Calculate number of dimes.
while cents >= 0.10:
    cents = cents - 0.10
    dimes = dimes + 1

# Calculate number of nickels.
while cents >= 0.05:
    cents = cents - 0.05
    nickels = nickels + 1

# Calculate number of pennies.
while cents >= 0.01:
    cents = cents - 0.01
    pennies = pennies + 1

coins = quarters + dimes + nickels + pennies
print("Coins returned: ", coins)