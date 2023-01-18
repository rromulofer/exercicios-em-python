n = str(input('Typer a name: '))
s = n.split()
print('First name: {}'.format(s[0]))
print('Last name: {}'.format(s[len(s)-1]))