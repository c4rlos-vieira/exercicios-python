import math

ano = int(input('Digite um ano: '))

if ano % 4 and ano % 400 or ano % 100 != 0:
    print('Esse ano é bissexto')
else:
    print('Esse ano não é bissexto')
