# Autor: Rômulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criação: 25/01/23
# Curso em Vídeo

from random import randint

r = randint(1, 6)
n = int(input('Tente acertar o número: '))

while n != r:
    n = int(input('Você errou, tente novamente: '))

print('Você acertou!!!')