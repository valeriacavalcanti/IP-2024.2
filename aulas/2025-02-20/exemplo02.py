"""
    trocar os caracteres especiais por '*'
"""

st = 'senha123eita0456!!!??%%%segura159753'
nova_st = ''

for i in range(len(st)):
    if st[i].isalnum() == True:
        nova_st += st[i]
    else:
        nova_st += '*'

    print(nova_st)
