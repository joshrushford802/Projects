import sys
import inflect

eng = inflect.engine()
ids = []


while True:
    try:
        inp = input("Name: ")
        ids.append(inp)
    except EOFError:
        break

print()
print("Adieu, adieu, to " + eng.join(ids))