n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
op = 0
while op != 5:
    print('''    [1]SOMAR
    [2]MULTIPLICAR
    [3]MAIOR
    [4]NOVOS NÚMEROS
    [5]SAIR DO PROGRAMA''')
    op = int(input('Digite uma opção: '))
    if op == 1:
        print('Resposta: {}'.format(n1+n2))
    elif op == 2:
        print('Resposta: {}'.format(n1 * n2))
    elif op == 3:
        if n1 > n2:
            print('Resposta: {}'.format(n1))
        else:
            print('Resposta: {}'.format(n2))
    elif op == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
print('-----FIM-----')