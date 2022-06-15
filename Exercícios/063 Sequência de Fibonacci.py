f = int(input('Quantos termos você quer mostrar? '))
cont = 3
n1 = 0
n2 = 1
n3 = 0
print('{} ➔ {}'.format(n1, n2), end='')
while cont <= f:
    n3 = n1 + n2
    print(' ➔ {}'.format(n3), end='')
    n1 = n2
    n2 = n3
    cont += 1
print(' ➔ FIM')