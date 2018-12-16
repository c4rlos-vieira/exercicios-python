print('Veja o preço do produto conforme a ondição de pagamento')
print('-' * 45 ,"""
Para pagar à vista no dinheiro ou cheque, digite: 1
À vista no cartão, digite 2
Até 2x no cartão, digite 3
3x ou mais no cartão, digite 4 
""", '-' * 45)
preço = float(input('Digite o preço: '))
metodo = int(input('Digite a forma de pagamento: '))

if metodo == 1:
    print('Você pagará R${} por pagar à vista'.format(preço * (1 - 0.1)))
elif metodo == 2:
    print('Você pagará R${} por pagar à vista com o cartão.'.format(preço * (1 - 0.05)))
elif metodo == 3:
    print('Você pagará R${} em até 2x no cartão.'.format(preço))
elif metodo == 4:
    print('Em 3x ou mais parcelas no cartão, você pagará R${}'.format(preço * (1 + 0.2)))
else:
    print('')