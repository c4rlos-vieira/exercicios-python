import random

alea = random.randint(0, 5)

print('Tente adivinhar o número entre 0 e 5 que o computador pensou')
print(""".
.
.
Pronto, tente adivinhar agora""")
numero = int(input('Coloque seu palpite aqui: '))
print('Você venceu!!!!!' if numero == alea else 'VocÊ perdeu :c')
print('-' * 20 ,'Fim', '-' * 20)
