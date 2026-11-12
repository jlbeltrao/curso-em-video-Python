dias = int(input('Por quantos dias o carro foi alugado? '))
kms = float(input('Quantos km foram percorridos? '))
valor_diaria = float(60)
valor_km = float(0.15)

print('O total a pagar é R${:.2f}.'.format((dias*valor_diaria)+(kms*valor_km)))