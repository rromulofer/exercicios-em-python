cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    num = int(input('Digite um número entre 0 e 10: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente:')
print(f'o número escolhido foi {cont[num]}')