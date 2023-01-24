# Autor: Rômulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criação: 24/01/23
# Curso em Vídeo

p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
d = (p + (10-1) * r)
for x in range(p, d+r, r):
    print('{}'.format(x), end=' > ')
