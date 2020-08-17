import re

final = re.findall('\/\/(.*)', input('Insira um código e um comentário utilizando //: '))

if final:
    print('Seu comentário é:', str(final[0].replace('"', '')))
else:
    print('Não encontramos seu comentário :(')