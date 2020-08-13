import re

final = re.findall('".*"', input('Insira uma frase com "" em uma palavra determinada: '))

if final:
    print('Sua palavra selecionada é: ' + str(final[0].replace('"', '')))
else:
    print('Não encontramos sua palavra :(')