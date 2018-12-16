preco = float(input('Coloque o preço do produto aqui e veja o quanto ganhou de desconto: '))
i = float(0.05)
desconto = preco * (1 - i)
print('Você pagará o valor de {} com {}% de desconto'.format(desconto, i * 100))
