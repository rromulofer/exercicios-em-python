soma=0
cont=0
for x in range(1,7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você digitou {} números pares, soma: {}'.format(cont, soma))
