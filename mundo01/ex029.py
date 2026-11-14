speed = int(input('Digite a velocidade do carro: '))

if speed > 80:
    print('Você foi multado.\nO valor da multa é R${:.2f}.'.format((speed-80)*7.00))
