idade = int(input('Digite a idade do atleta: '))

if idade<=9:
    print('Mirim')
elif idade>9 and idade<=14:
    print('Infantil')
elif idade > 14 and idade <= 19:
    print('Junior')
elif idade>19 and idade<=25:
    print('Sênior')
elif idade>25:
    print('Master')
