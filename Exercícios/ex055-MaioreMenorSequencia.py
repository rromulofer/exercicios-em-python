# Autor: Rômulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criação: 17/02/23
# Curso em Vídeo

me = 0
ma = 0
for x in range(1,4):
    p = float(input('Digite o peso em kg: '))
    if x == 1:
        ma = p
        me = p
    else:
        if p > ma:
            ma = p
        if p < me:
            me = p
print('Maior:{} Menor:{}'.format(ma, me))
