n = str(input('Type a name: ')).upper()
print('Amount of A: {}'.format(n.count('A')))
print('First A: {}'.format(n.find('A')+1))
print('Last A: {}'.format(n.rfind('A')+1))