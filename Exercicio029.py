velocidade = float(input('Qual a velocidade do veículo? '))
if velocidade > 80.0:
    print('Você foi multado e valor da multa é: R${:.2f}'.format((velocidade - 80.0) * 7.0))
else:
    print('Este veículo está no nível aceitável de velocidade. Portanto, está livre!')

print('-' * 20, 'FIM', '-' * 20)
