km_viagem = int(input('Qual a distância da viagem em kms? '))

""" if km_viagem < 200:
    print('A passagem para essa viagem custa R${:.2f}'.format(km_viagem*0.5))
else:
    print('A passagem para essa viagem custa R${:.2f}'.format(km_viagem*0.45)) """
""" 
if km_viagem < 200:
    preco = km_viagem*0.5
else:
    preco = km_viagem*0.45
 """
preco = km_viagem * 0.5 if km_viagem <= 200 else km_viagem * 0.45

print('A passagem para essa viagem custa R${:.2f}'.format(preco))