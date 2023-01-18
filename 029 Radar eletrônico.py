v = float(input('Type a vehicle speed: '))
if v>80:
    t = (v-80)*7
    print('---You were fined---')
    print('Fine amount R${}'.format(t))
else:
    print('---You were not fined---')