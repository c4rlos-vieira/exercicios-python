import random

numa = int(random.randint(0, 9999))
print('-' * 30)
print(numa)
print("""{} Primeiro algarismo
{} Segundo algarismo
{} Terceiro algarismo
{} Quarto algarismo""".format(((numa // 1000) % 10), ((numa // 100)% 10), ((numa // 10) % 10), ((numa // 1) % 10)))
print('-' * 30)

