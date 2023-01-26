# Autor: Rômulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criação: 23/01/23
# Curso em Vídeo

y = int(input('Type a year: '))
if y%4==0 and y%100!=0 or y%400==0:
    print('{} is a leap year'.format(y))
else:
    print('{} isnt a leap year'.format(y))
