import cs50

print('What is the answer to the Great Question of Life, the Universe and Everything?')

answer = input()
ans = answer.strip().lower()

if ans != '42' and ans != 'forty-two' and ans != 'forty two':
    print('No')
else:
    print('Yes')