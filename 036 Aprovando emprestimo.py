valor = float(input('Valor da casa: '))
salario = float(input('Salário: '))
meses = int(input('Meses para pagar:'))

parcela = valor/meses
if parcela > (salario*0.30):
    print('---Empréstimo negado---')
else:
    print('---Empréstimo aceito---')