r1 = int(input('Digita o valor da reta 1: '))
r2 = int(input('Digita o valor da reta 2: '))
r3 = int(input('Digita o valor da reta 3: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('As retas \033[32mpodem\033[m formar um triângulo.')
    if r1 == r2 == r3:
        print('O triângulo é equilatero.')
    elif r1 == r2 != r3 or r1 != r2 == r3 or r1 == r3 != r2;
else:
    print('As retas {}não{} podem formar um triângulo'.format('\033[31m', '\033[m'))
