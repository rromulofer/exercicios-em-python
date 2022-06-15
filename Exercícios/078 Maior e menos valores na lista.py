valores = list()
maior = 0
menor = 0
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    if  cont == 0:
        maior = menor = valores[cont]
for v in valores:
    if v > maior:
        maior = v
    elif v < menor:
        menor = v

print(f'Valores digitados: {valores} \n Maior:{maior} \n Menor:{menor}')