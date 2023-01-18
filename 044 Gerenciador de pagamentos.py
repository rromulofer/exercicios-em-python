preco = float(input('Digite o preço do produto: '))
print('''Formas de pagamento:
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
op = int(input('Digite a forma de pagamento: '))

if op==1:
    preco = preco*0.90
    print('Valor final: {}'.format(preco))
elif op==2:
    preco = preco*0.95
    print('Valor final: {}'.format(preco))
elif op==3:
    print('Valor final: {}'.format(preco))
elif op == 4:
    preco = preco * 1.20
    print('Valor final: {}'.format(preco))