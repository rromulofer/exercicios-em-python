y = int(input('Type a year: '))
if y%4==0 and y%100!=0 or y%400==0:
    print('{} is a leap year'.format(y))
else:
    print('{} isnt a leap year'.format(y))
