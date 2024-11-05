# tempo início
hi = int(input('Hora início: '))
mi = int(input('Minuto início: '))
si = int(input('Segundo início: '))

# tempo fim
hf = int(input('Hora fim: '))
mf = int(input('Minuto fim: '))
sf = int(input('Segundo fim: '))

# converter para segundos
ti = (hi * 3600) + (mi * 60) + si
tf = (hf * 3600) + (mf * 60) + sf

# calcular o tempo de uso
tempo = tf - ti

# converter para h m s
h = tempo // 3600
m = (tempo % 3600) // 60
s = (tempo % 3600) % 60

# exibir
print(f'{h}:{m}:{s}')
print(h,m,s, sep = ':')
