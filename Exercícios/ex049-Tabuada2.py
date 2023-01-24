# Autor: Rômulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criação: 24/01/23
# Curso em Vídeo

print("\n Tabuada 2.0!")

n = int(input("\n Digite um número: "))

for cont in range(1, 11):
    print("{} x {} = {}".format(n, cont, n*cont))