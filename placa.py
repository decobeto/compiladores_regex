import re

placa = re.compile('^[a-zA-Z]{3}-[0-9]{3}')

entrada = input('\nDigite uma placa no padrão "AAA-1234": ')

if placa.match(entrada):
    print('A placa digitada "%s" está no padrão de veículos brasileiro.' % (entrada))
else:
    print('A placa digitada "%s" NÃO está no padrão de veículos brasileiro.' % (entrada))