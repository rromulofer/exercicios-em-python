from random import randint
r = randint(0, 5)
print('Pensei em um número entre 0 e 5')
n = int(input('Tente acertar: '))

if r==n:
    print('Você acertou')
else:
    print('Você errou')