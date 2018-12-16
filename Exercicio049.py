print('Descubra aqui a tabuada de qualquer número')
print('-' * 40)
num = int(input('Digite aqui um número inteiro: '))

for tab in range(1, 11):
    print('{} x {} = {}'.format(num, tab, num * tab))
