n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
t = n
cont = 1
while cont <= 10:
    print('{} > '.format(t), end='')
    t += r
    cont += 1
print('FIM!')