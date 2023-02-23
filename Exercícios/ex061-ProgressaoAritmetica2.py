# Autor: Rômulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criação: 22/02/23
# Curso em Vídeo

n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
t = n
cont = 1
while cont <= 10:
    print('{} > '.format(t), end='')
    t += r
    cont += 1
print('FIM!')
