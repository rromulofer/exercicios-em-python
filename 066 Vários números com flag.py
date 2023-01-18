cont = 0
soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    cont += 1
print('Foram digitados {} números e a soma é {}'.format(cont, soma))