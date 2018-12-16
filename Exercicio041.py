atleta = int(input('Digite a sua idade e diremos qual categoria você se encaixa: '))

if atleta <= 9:
    print('Você é Mirim')
elif atleta <= 14:
    print('Você é Infantil')
elif atleta <= 20:
    print('Você é Sênior')
else:
    print('Você é categoria Master')
