import cs50

input = input("Input: ")

if input[1:].islower():
    output = input.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')
else:
    output = input.replace('A', '').replace('E', '').replace('I', '').replace('O', '').replace('U', '')

print("Output: ", output)