from random import randint
r = randint(1, 6)
n = int(input('Tente acertar: '))
while n != r:
    n= int(input('Você errou, tente novamente: '))
print('Você acertou')
