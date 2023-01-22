# Autor: Rômulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criação: 20/01/23
# Curso em Vídeo

d = int(input('Dias alugados: '))
km = float(input('Km rodados:'))
p = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(p))