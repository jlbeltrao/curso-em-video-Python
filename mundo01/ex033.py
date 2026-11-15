num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

numeros = [num1, num2, num3]
numeros.sort()
print('O menor número é o {}, e o maior é o {}'.format(numeros[0], numeros[-1]))
