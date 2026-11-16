idade = int(input('Digite sua idade: '))

if idade < 18:
    print('Você ainda vai se alistar no exército')
elif idade == 18:
    print('Está na hora de se alistar.')
else:
    print('Já passou do tempo do alistamento.')