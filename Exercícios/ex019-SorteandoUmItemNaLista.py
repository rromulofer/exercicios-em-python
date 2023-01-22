# Autor: Rômulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criação: 21/01/23
# Curso em Vídeo

from random import choice
n1 = str(input('First student: '))
n2 = str(input('Second student: '))
n3 = str(input('Third student: '))
n4 = str(input('Fourth student: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('Chosen student {}'.format(escolhido))
