d = int(input('Dias alugados: '))
km = float(input('Km rodados:'))
p = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(p))