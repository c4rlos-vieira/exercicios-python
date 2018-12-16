largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))

area = largura * altura

tinta = float(area)/2

print('Para {}m², você gastará {} litros de tinta'. format(area, tinta))
