print('Monte a sua progressão aritmética')
p1 = int(input('Digite o primeiro número da sequência: '))
razão = int(input('Digite a razão da sequência: '))
termo = int(11)

for seq in range(p1, (p1 + ((termo - 1)) * razão), razão):
    print(seq)
