# Autor: Rômulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criação: 23/01/23
# Curso em Vídeo

s = float(input('Type the salary: '))
if s>1250:
    n = s+(s*10/100)
else:
    n = s+(s*15/100)
print('Salary increased to R${:.2f}'.format(n))