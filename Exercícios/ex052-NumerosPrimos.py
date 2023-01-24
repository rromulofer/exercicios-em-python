# Autor: Rômulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criação: 24/01/23
# Curso em Vídeo

cont = 0
n = int(input('Digite um número: '))
for x in range(1, 11):
    if n % x == 0:
        cont += 1
        print('\033[32m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}'.format(x), end=' ')

if cont == 2:
    print('\n\033[mO número é primo!')
else:
    print('\n\033[mO número não é primo!')
