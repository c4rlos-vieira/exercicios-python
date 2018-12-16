import math
a = math.radians(float(input('Digite um ângulo qualquer entre 0 e 360: ')))

print('-' * 20)
print('Estas são as medidas do angulo {:.2f}º: \n- Seno: {:.2f} \n- Cosseno: {:.2f} \n- Tangente: {:.2f}'.format(math.degrees(a), math.sin(a), math.cos(a), math.tan(a)))
print('-' * 20)
