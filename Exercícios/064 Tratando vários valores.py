n = soma = 0
n = int(input('Digite um número [999 para]: '))
while n != 999:
    soma += n
    n = int(input('Digite um número [999 para]: '))
print('Soma: {}'.format(soma))

