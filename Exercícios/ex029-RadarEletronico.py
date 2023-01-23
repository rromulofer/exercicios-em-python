# Autor: Rômulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criação: 23/01/23
# Curso em Vídeo

v = float(input('Type a vehicle speed: '))
if v > 80:
    t = (v-80)*7
    print('---You were fined---')
    print('Fine amount R${}'.format(t))
else:
    print('---You were not fined---')
