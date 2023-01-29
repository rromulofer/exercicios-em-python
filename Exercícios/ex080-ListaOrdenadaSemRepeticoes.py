# Autor: Rômulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criação: 28/01/23
# Curso em Vídeo

lista = list()

for cont in range(0, 5):
    n = int(input("Digite um valor: "))
    if cont == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram: {lista}')
