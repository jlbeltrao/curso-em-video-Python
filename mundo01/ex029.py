speed = int(input('Digite a velocidade do carro: '))

if speed > 80:
    print('Você excedeu o limite de 80km/h e foi multado.\nO valor da multa é R${:.2f}.'.format((speed-80)*7.00))
