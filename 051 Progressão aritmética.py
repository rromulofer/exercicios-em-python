p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
d = (p + (10-1) * r)
for x in range(p, d+r, r):
    print('{}'.format(x), end=' > ')