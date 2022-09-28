print('=' * 30)
print('CAIXA ELETRONICO')
print('=' * 30)
valor = int(input('Digite o valor a ser sacado: '))
total = valor
ced = 50
tced = 0
while True:
    if total >= ced:
        total -= ced
        tced += 1
    else:
        if tced > 0:
            print(f'Total de {tced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        tced = 0
        if total == 0:
            break