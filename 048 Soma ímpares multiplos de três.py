soma=0
cont=0
for x in range(1, 501, 2):
    if x % 3 == 0:
        soma += x
        cont += +1
print('Soma dos números {} impares multiplos de 3: {} '.format(cont, x))