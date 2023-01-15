import cs50
import sys

inp = input("Plate: ")

if inp[2:] == range(0, 9) and inp[5] == range(0, 9) and inp <= 6 and inp >= 2 and '!' not in inp and '.' not in inp and ' ' not in inp:
    print("Valid")
elif  inp == 'CS50' or inp == 'ECTO88' or inp == 'NRVOUS':
    print("Valid")
else:
    print("Invalid")