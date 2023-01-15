import math

text = input("Enter Text: ")

sentences = 0
words = 0
letters = 1

for i in range(len(text)):
    if text[i] == "." or text[i] == "!" or text[i] == "?":
        sentences = sentences + 1
    elif text[i] == " " or text[i] == "\0":
        words = words + 1
    elif text[i] != 22 and text[i] != "'" and text[i] != "(" and text[i] != ")" and text[i] != "`" and text[i] != "-" and text[i] != ":" and text[i] != ";" and text[i] != "/":
        letters = letters + 1

L = letters / words * 100
S = sentences / words * 100
grade = math.floor(0.0588 * L - 0.296 * S - 15.8 - 0.85)

if grade < 1:
    print("Before Grade 1\n")
elif grade > 16:
    print("Grade 16+\n")
else:
    print("Grade ", grade)