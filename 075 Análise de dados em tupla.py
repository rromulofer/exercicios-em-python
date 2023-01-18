par = 0
imp = 0
cont = 0
n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite outro número: ')))
print(f'Valores digitados: {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O valor 3 apareceu na posição {n.index(3)+1}º')
else:
    print('O valor 3 não foi digitado')

print('Valores Pares: ')
for cont in n:
    if cont % 2 == 0:
        print(cont)
