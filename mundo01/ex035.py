r1 = int(input('Digita o valor da reta 1: '))
r2 = int(input('Digita o valor da reta 2: '))
r3 = int(input('Digita o valor da reta 3: '))

#Código para triângulo ratângulo
""" retas = [reta1, reta2, reta3]
retas.sort()

if retas[0]**2 + retas[1]**2 == retas[2]**2:
    print('As retas podem formar um triângulo retângulo.')
else:
    print('As retas não podem formar um triângulo retângulo.') """

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('As retas podem formar um triângulo.')
else:
    print('As retas não podem formar um triângulo')