nome = str(input('Digite seu nome completo: '))
cespaço = int(len(nome))
sespaço = int(nome.count(' '))
primeiron = nome.split()
print(nome.upper())
print(nome.lower())
print('Esta string tem {} sem contar o espaços'.format((cespaço - sespaço)))
print('O primeiro nome tem {} letras.'.format(len(primeiron[0])))
