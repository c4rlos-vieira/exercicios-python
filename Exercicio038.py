from random import randint
num1 = randint(1, 10)
num2 = randint(1, 10)

if num1 > num2:
    print('{} é maior que {}!'.format(num1, num2))
elif num1 == num2:
    print('Os números {} e {} são iguais.'.format(num1, num2))
else:
    print('O numero {} é maior que {}.'.format(num2, num1))
