frase = str(input('Digite uma frase: ')).strip()
print('A letra "A" aparece {} vezes na frase.'.format(frase.lower().count('a')))
print('A primeira letra "A" aparece na posição {}.'.format(frase.lower().find('a')))
print('A última letra "A" aparece na posição {}.'.format(frase.lower().rfind('a')))