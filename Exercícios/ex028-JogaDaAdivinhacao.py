# Autor: Rômulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criação: 23/01/23
# Curso em Vídeo

from random import randint
r = randint(0, 5)
print('Pensei em um número entre 0 e 5')
n = int(input('Tente acertar: '))

if r==n:
    print('Você acertou')
else:
    print('Você errou')