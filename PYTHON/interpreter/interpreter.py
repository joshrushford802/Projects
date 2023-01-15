import cs50

inpit = input('Expression: ')

inp = inpit.split(' ')

if '+' in inp:
    compute = int(inp[0]) + int(inp[2])
elif '-' in inp:
    compute = int(inp[0]) - int(inp[2])
elif '*' in inp:
    compute = int(inp[0]) * int(inp[2])
elif '/' in inp:
    compute = int(inp[0]) / int(inp[2])

print(float(compute))