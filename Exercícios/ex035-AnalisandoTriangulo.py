# Autor: Rômulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criação: 23/01/23
# Curso em Vídeo

s1 = float(input('Type segment 1: '))
s2 = float(input('Type segment 2: '))
s3 = float(input('Type segment 3: '))
if s1<s2+s3 and s2<s1+s3 and s3<s2+s1:
    print('These segments form a triangle')
else:
    print('These segments dont form a triangle')