import random
print('JoKenPô')

movimentos  = ['pedra','papel','tesoura']
pc = random.choice(movimentos)

user = str(input('Faça sua jogada, escolha entre pedra, papel ou tesoura: ')).strip()

print('Sua Escolha: {} vs PC Escolha: {}'.format(user, pc))

if pc == 'pedra' and user == 'papel':
    print('Você ganhou!')
elif pc == 'pedra' and user == 'tesoura':
    print('Você perdeu!')
elif pc == 'tesoura' and user == 'pedra':
    print('Você Ganhou!')
elif pc == 'tesoura' and user == 'papel':
    print('Você perdeu!')
elif pc == 'papel' and user == 'pedra':
    print('Você perdeu!')
elif pc == 'papel' and user == 'tesoura':
    print('Você ganhou!')
else:
    print('Deu empate')
