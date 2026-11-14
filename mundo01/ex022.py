import time
nome = str(input('Escreva seu nome: '))

print('Analisando seu nome...')
time.sleep(1)
print('Seu nome em maiusculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
#print('Seu nome tem {} letras.'.format(len(nome.replace(' ', ''))))
print('Seu nome tem {} letra.'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format(nome.split()[0].capitalize(), len(nome.split()[0])))
