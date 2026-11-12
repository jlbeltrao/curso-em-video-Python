import math

cat1 = int(input('Digite o valor do cateto oposto: '))
cat2 = int(input('Digite o valor do cateto adjacente: '))
hip = math.sqrt(cat1**2 + cat2**2)

print('A hipotenusa é {:.4f}.'.format(hip))