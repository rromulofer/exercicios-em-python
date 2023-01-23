# Autor: Rômulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criação: 23/01/23
# Curso em Vídeo

n = str(input('Enter a name: '))
s = n.split()
print('First name: {}'.format(s[0]))
print('Last name: {}'.format(s[len(s)-1]))