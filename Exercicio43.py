print('Olá, vamos calcular seu IMC, por favor nos passe alguns dados')
massa = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = massa / (altura ** 2)

if imc < 18.5:
    print('Ihhh, você tá muito abaixo do peso.')
elif 18.5 <= imc <= 25:
    print('Você está com o seu peso ideal, mas se atente ao seu percentual de gordura')
elif 25 < imc <= 30:
    print('Ihh, tá com sobrepeso. Bora correr?')
elif 30 < imc <= 40:
    print('Ih, tá com obesidade. Procure um médico urgente e uma academia também')
else:
    print('Nossa, você está com obesidade mórbida')
