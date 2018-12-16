num = int(input('Digite um número para saber se ele é primo: '))
for seq in range(0, 1):
    if num % 2 == 0 or num == 1:
        print('Este não é um número primo')
    elif num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        print('Este número não é primo')
    elif num == 3 or num == 5 or num == 7 or num == 2:
        print('Este é um número primo')
    else:
        print('Este é um número primo')
