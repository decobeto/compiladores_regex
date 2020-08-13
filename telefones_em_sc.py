import re

telefone = input('Digite no padrão "(48) 99178-1296": ')

print(telefone)

if re.match('^\([4]{1}[7-9]{1}\)', telefone):
    print('Este é um número de Santa Catarina, Brasil')
else:
    print('Este não é um número válido em SC')