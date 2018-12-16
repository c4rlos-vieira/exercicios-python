dist = float(input("""Vai vaijar é?! Que bacana!
Conta  para mim a distância que tu quer viajar 
para eu poder fazer o calculo da sua passagem: """))
print("""
Calculando ...
""")

if dist <= 200.0:
    print('Sua passagem custará R${:.2f} para esta distância.'.format(dist * 0.50))
else:
    print('Para está distância, sua passagem custará R${:.2f}'.format(dist * 0.45))
