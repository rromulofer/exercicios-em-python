from datetime import date
ma=0
me=0
atual = date.today().year
for x in range(0, 5):
    ano = int(input('Digite o ano de nascimento: '))
    if (atual-ano) >= 18:
        ma += 1
    else:
        me += 1
print('{} são maiores de idade'.format(ma))
print('{} são menores de idade'.format(me))