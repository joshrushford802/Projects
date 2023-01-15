import random


def main():
    generate_integer(get_level())


def get_level():
    while True:
        try:
            level = int(input("Level: "))

            if level not in range(1, 4):
                pass
            else:
                break
        except ValueError:
            pass

    return level



def generate_integer(level):
    i = 0

    while i < 9:
        try:
            n = 0

            if level == 1:
                rand_num1 = random.randint(0, 9)
                rand_num2 = random.randint(0, 9)
                print(f"{rand_num1} + {rand_num2} = ", end='')
                answer = int(input())
                while True:
                    if rand_num1 + rand_num2 == answer:
                        break
                    elif n == 2:
                        print(f"{rand_num1} + {rand_num2} =", rand_num1 + rand_num2)
                        break
                    else:
                        print("EEE")
                        print(f"{rand_num1} + {rand_num2} = ", end='')
                        answer = int(input())
                        n += 1
            elif level == 2:
                rand_num1 = random.randint(10, 99)
                rand_num2 = random.randint(10, 99)
                print(f"{rand_num1} + {rand_num2} = ", end='')
                answer = int(input())
                while True:
                    if rand_num1 + rand_num2 == answer:
                        break
                    elif n == 2:
                        print(f"{rand_num1} + {rand_num2} =", rand_num1 + rand_num2)
                        break
                    else:
                        print("EEE")
                        print(f"{rand_num1} + {rand_num2} = ", end='')
                        answer = int(input())
                        n += 1
            if level == 3:
                rand_num1 = random.randint(100, 999)
                rand_num2 = random.randint(100, 999)
                print(f"{rand_num1} + {rand_num2} = ", end='')
                answer = int(input())
                while True:
                    if rand_num1 + rand_num2 == answer:
                        break
                    elif n == 2:
                        print(f"{rand_num1} + {rand_num2} =", rand_num1 + rand_num2)
                        break
                    else:
                        print("EEE")
                        print(f"{rand_num1} + {rand_num2} = ", end='')
                        answer = int(input())
                        n += 1
        except ValueError:
            print("EEE")

        i = i + 1


if __name__ == "__main__":
    main()