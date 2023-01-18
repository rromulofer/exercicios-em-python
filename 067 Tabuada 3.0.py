while True:
    n = int(input('Digite um número: '))
    if n < 0:
        break
    for x in range(1, 11):
        print('{} x {} = {}'.format(n, x, (n*x)))

