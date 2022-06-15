km = float(input('Enter the trip distance in kilometers: '))
if km<=200:
    print('Value: R${}'.format(km*0.50))
else:
    print('Value: R${}'.format(km*0.45))