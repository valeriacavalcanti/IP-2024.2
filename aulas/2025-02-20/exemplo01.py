'''
    trocar as vogais por '*'
'''

st = 'senha123eita0456!!!??%%%segura159753'

vogais = 'aeiouAEIOU'

for i in range(len(vogais)):
    st = st.replace(vogais[i],'*')
    print(st)
