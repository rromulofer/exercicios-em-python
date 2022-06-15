n = int(input('Digite o número um número: '))
r = 0
cont = 0
while n > cont:
    print('{}'.format(n), end='')
    print(' x ' if n > 1 else ' = ', end='')
    r += n
    n -= 1
print(r)
