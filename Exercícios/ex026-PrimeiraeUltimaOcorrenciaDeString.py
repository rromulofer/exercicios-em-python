# Autor: Rômulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criação: 23/01/23
# Curso em Vídeo

n = str(input('Enter a name: ')).upper()
print('Amount of A: {}'.format(n.count('A')))
print('First A: {}'.format(n.find('A')+1))
print('Last A: {}'.format(n.rfind('A')+1))