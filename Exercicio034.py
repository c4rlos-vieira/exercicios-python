salario = float(input('Quanto é o seu salário? '))

if salario >= 1250.00:
    print('Seu novo salário é de R${:.2f}'.format(salario * (1 + 0.15)))
else:
    print('Seu novo salário é de R${:.2f}'.format(salario * (1 + 0.1)))
