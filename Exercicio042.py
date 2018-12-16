from math import fabs
a = float(input('Digite a medida da primeira reta: '))
b = float(input('Digite a medida da segunda reta: '))
c = float(input('Digite a medida da terceira reta: '))

if fabs(b - c) < a < (b + c) and fabs(a - c) < b < (a + c) and fabs(a - b) < c < (a + b):
    print('Você pode montar um triângulo com essas medidas')
else:
    print('Você não pode montar um triângulo com essas medidas')

if a == b == c:
    print('Você pode montar um triângulo equilátero')
elif a == b or b == c or a == c:
    print('Você pode montar um triângulo isosceles')
else:
    print('Você pode montar um triângulo escaleno')

