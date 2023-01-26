# Autor: Rômulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criação: 23/01/23
# Curso em Vídeo

km = float(input('Enter the trip distance in kilometers: '))
if km<=200:
    print('Value: R${}'.format(km*0.50))
else:
    print('Value: R${}'.format(km*0.45))