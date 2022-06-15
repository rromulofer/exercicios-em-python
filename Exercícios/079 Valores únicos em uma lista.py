numeros = list()

while True:
    n  = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado!')
    else:
        print('Valor já existe!')
    p = str(input('Deseja continua? [S/N]'))
    if p in 'Nn':
        break
numeros.sort()
print(f'Valores digitados: {numeros}')