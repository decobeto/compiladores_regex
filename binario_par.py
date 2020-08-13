# Expressões regular que reconhece Binários pares
import re

if re.match('.*?([0]+)$', input('Entre um número binário: ')):
    print('Parabéns é um binário par!')
else:
    print('Esse número não é binario par :(')