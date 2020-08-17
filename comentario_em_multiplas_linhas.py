import re

final = re.findall('\/\*.*\*\/', input('Insira um código com um comentário de múltiplas linhas(/* */) : '))

if final:
    print('Seu comentário é:', str(final[0].replace('"', '')))
else:
    print('Não encontramos seu comentário :(')