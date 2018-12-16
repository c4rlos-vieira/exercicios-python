nome = str(input('Olá, qual o seu nome? '))
nota1 = float(input('Qual foi a nota da sua primeira prova? '))
nota2 = float(input('Qual foi a nota da sua segunda prova? '))
print('Olá, {} \n Primeira prova: {} \n Segunda prova: {} \n Média final: {}'.format(nome, nota1, nota2, ((nota1+nota2)/2)))
