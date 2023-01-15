import cs50

greeting = input("Greeting: ")
greet = greeting.strip()

if 'Hello' in greet:
    print('$0')
elif greet[0] == 'H':
    print('$20')
else:
    print('$100')