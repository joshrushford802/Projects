import random

while True:
    try:
        inp = int(input("Level: "))

        if inp >= 0:
            break
        else:
            pass
    except ValueError:
        pass

random_num = random.randint(0, inp)

while True:
    try:
        guess = int(input("Guess: "))

        if guess < random_num:
            print("Too small!")
            continue
        elif guess > random_num:
            print("Too large!")
            continue
        elif guess == random_num:
            print("Just right!")
            break
    except ValueError:
        pass