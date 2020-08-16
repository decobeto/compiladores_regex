import re

resposta  = re.findall('@\w+.br$|@\w+.com.br$', input('Digite um e-mail com domínio ".br" ou ".com.br": '))

if resposta:
    print('O e-mail digito é válido.')
else:
    print('O e-mail digitado não é válido')