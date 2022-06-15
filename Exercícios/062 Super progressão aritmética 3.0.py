n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
cont = 1
fim = 10
mais = 1
while mais != 0:
    while cont <= fim:
        print('{} > '.format(n), end='')
        n += r
        cont += 1
    print('FIM!')
    mais = int(input('Deseja que o programa mostre mais números?'))
    fim += mais
print('---FIM DO PROGRAMA---')



