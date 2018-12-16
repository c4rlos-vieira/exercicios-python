print('\033[1;34mOlá, vamos verififcar se o sua solicitação de crédito imobiliário será ou não aprovada :)\033[m')
print("""\033[1;34mPrecisaremos dos seguintes dados:
- Valor da Casa
- Seu salário
- Quantos anos de prestação pretende pagar.
.

Então, vamos lá...\033[m""")
casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
prestação = float(input('Quantos anos pretende pagar? '))
print('\033[1;34mCalculando ...\033[m')

if casa/(prestação * 12) < salario * 0.3:
    print('\033[32mParabéns!!!! Seu crédito foi aprovado. O valor das prestações será de {:.2f} durante {:.0f} meses.\033[m'.format(casa/(prestação * 12), prestação * 12))
elif casa/(prestação * 12) == salario * 0.3:
    print('\033[33mParabéns, seu crédito foi aprovado! Mas, cuidado! As prestações são {:.2f} durante {:.0f} meses e elas pegam 30% do seu salário.\033[m'.format(casa/(prestação * 12), prestação * 12))
else:
    print('\033[31mQue pena, mas não aprovamos o seu empréstimo. As prestações de {:.2f} ficaram altas demais para o seu salário.\033[m'.format(casa/(prestação * 12), prestação * 12))
