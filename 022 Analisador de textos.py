name = str(input('Type your name: ')).strip()
print('Uppercase name: {}'.format(name.upper()))
print('Lowercase name: {}'.format(name.lower()))
print('Total letters: {}'.format(len(name) - name.count(' ')))
#print('First name has {} letters. '.format(name.find(' ')))
s = name.split()
print('First name has {} letters.'.format(len(s[0])))