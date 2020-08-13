import re

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

entrada = text_to_bits(input('Digite sua palavra preferida: '))

print((entrada.len))
print('Palavra em binário: ' + entrada)

if re.match('.*?([00]+)$', entrada):
    print('Parabéns é uma palavra em binário!')
else:
    print('Está palavra (binário) não termina em 00')
