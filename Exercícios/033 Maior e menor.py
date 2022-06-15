n1 = int(input('Type a number: '))
n2 = int(input('Type another number: '))
n3 = int(input('Type another number: '))
ma = n1
if n2>n1 and n2>n3:
    ma = n2
if n3>n1 and n3>n2:
    ma = n3

me = n1
if n2<n1 and n2<n3:
    me = n2
if n3<n1 and n3<n2:
    me = n3

print('{} is a bigger number and {} is a smaller number'.format(ma,me))



