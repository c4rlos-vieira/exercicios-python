import math
co = float(input('Qual a medida do cateto oposto? '))
ca = float(input('Qual a medida do cateto adjacente? '))

print('-' * 16)
print('As medidas deste triângulo são: \n- Cateto oposto: {0} \n- Cateto Adjacente: {1} \n- Hipotenusa: {2:.3f}'.format(float(co), float(ca), math.hypot(co, ca)))
print('-' * 16)
