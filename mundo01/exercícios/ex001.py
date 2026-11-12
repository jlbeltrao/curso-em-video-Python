#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

metragem = float(input('Qual o tamanho da área a ser pintada ? '))

cobertura_tinta_m2 = float(6)
lata_tinta_lts = int(18)
lata_tinta_preco = 80
galao_tinta_lts = float(3.6)
galao_tinta_preco = 25

qud_tinta_lts = metragem / cobertura_tinta_m2

print('Para pintar {}m², você precisa de {:.2f}L de tinta.'.format(metragem, qud_tinta_lts))
print('Você precisa de {} lata(s). Irá sobrar L.'.format(qud_tinta_lts//lata_tinta_lts))

print(qud_tinta_lts /lata_tinta_lts)