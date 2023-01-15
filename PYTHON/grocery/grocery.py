grocery_list = {}

while True:
    try:
        inp = str(input())
        inp = inp.upper()

        if inp not in grocery_list:
            grocery_list[inp] = 1
        else:
            grocery_list[inp] = grocery_list[inp] + 1
            
    except ValueError:
        pass
    except EOFError:
        for value, key in grocery_list.items():
            print(key, value)
        break