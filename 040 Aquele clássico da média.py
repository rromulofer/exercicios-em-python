p1 = float(input('Digite a nota da p1: '))
p2 = float(input('Digite a nota da p2: '))
m = (p1+p2)/2

if m>7.0:
    print('---Aprovado---')
elif m>5.0 and m<6.9:
    print('---Recuperação---')
else:
    print('---Reprovado---')
