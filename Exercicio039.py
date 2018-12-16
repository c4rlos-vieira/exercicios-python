from math import fabs
print('Eae, jovem. Preocupado com o alistamento militar?')
idade = int(input('Coloque aqui a sua idade e nos diremos para você se falta muito tempo, se já está na hora ou se jaá passou da hora: '))

if idade < 17:
    print('Falta um tempo para você se preocupar com isso! Falta: {} ano(s)'.format(fabs(18 - idade)))
elif idade == 18:
    print('Está na hora de você se apresentar na junta militar.')
else:
    print('Já passou {} ano(s) da hora de você ir na junta militar, procure uma mais próxima e regularize sua situação.'.format(fabs(18 - idade)))
