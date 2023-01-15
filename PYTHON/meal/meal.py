import cs50

inpit = input('What time is it? ')

inp = inpit.split(':')

if inp[0] == '7':
    print('breakfast time')
elif inp[0] == '8' and inp[1] == '00':
    print('breakfast time')
elif inp[0] == '12':
    print('lunch time')
elif inp[0] == '13' and inp[1] == '00':
    print('lunch time')
elif inp[0] == '18':
    print('dinner time')
elif inp[0] == '19' and inp[1] == '00':
    print('dinner time')