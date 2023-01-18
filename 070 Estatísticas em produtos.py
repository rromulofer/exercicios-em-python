print("----------MERCADO----------")
total = 0
caro = 0
barato = ' '
menor = 0
cont = 0
while True:
    pro = str(input('Produto: '))
    pre = float(input('Valor: '))
    cont += 1
    if cont == 1:
        menor = pre
        barato = pro
    else:
        if pre < menor:
            menor = pre
            barato = pro
    total += pre
    if pre > 1000:
        caro += 1
    op = ' '
    op = str(input('Continuar?[s/n]'))
    if op == 'n':
        break


print('\nTotal gasto: {}'.format(total))
print('Produtos que custaram mais de R$1000: {}'.format(caro))
print(f'Produto mais barato: {barato} e custa {menor}')

print("----------FIM----------")