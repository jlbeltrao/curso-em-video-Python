peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura (em cm): '))/100

imc = peso / (altura ** 2)

print('Seu IMC é {:.2f}.'.format(imc))

if imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Peso ideal.')
elif 25 <= imc < 30:
    print('Sobrepeso.')
elif 30 <= imc < 40:
    print('Obesidade.')
elif imc > 40:
    print('Obesidade mórbida.')

print('Seu peso ideal é {:.2f}kg a {:.2f}kg.'.format(18.5*(altura**2), 25*(altura**2)))