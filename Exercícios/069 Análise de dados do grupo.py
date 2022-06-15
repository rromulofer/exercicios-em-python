a = 0
b = 0
c = 0
while True:
    id = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo: [M/F]')).strip().upper()[0]
    if id > 18:
        a += 1
    if sexo == "M":
        b += 1
    if sexo == "F" and id < 20:
        c += 1
    op = ' '
    while op not in "SN":
        op = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if op == "N":
        break

print("Pessoas com mais de 18 anos: {} ".format(a))
print("Total de homens: {}".format(b))
print("Mulheres com menos de 20 anos: {}".format(c))




