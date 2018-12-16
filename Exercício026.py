frase = str(input('Digite uma frase qualquer: ')).strip()

print("""Nesta frase aparece:
{} letras "a"; 
Essa letra aparece pela primeira vez em: {} 
E aparece pela última vez em: {}""".format(frase.lower().count('a'),frase.lower().find('a'), frase.lower().rfind('a')))