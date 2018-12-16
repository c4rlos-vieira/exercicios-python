soma = 0
vezes = 501
for s in range(1, vezes):
    if s % 2 == 1 and s % 3 == 0:
        print(s)
    tudo = soma + s * vezes
    print(tudo)
