nota = float(input('Coloque aqui as suas sotas e veremos se você está ferrado: '))
if nota < 5:
    print('\033[31mTá reprovado!\033[m')
elif 5 <= nota < 7:
    print('Na risca, hein, lek. Ta só de recuperação')
else:
    print('Aprovadíssimo com louvor!')
