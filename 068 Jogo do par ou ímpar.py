from random import randint
v = 0
while True:
    joga = int(input('Digite um valor: '))
    comp = randint(0, 11)
    total = joga + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {joga} e o computador {comp}. Total {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ GANHOU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ GANHOU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
print('Total de vitórias: {}'.format(v))