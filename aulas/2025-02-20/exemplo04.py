def vogal(simbolo):
    vogais = 'aeiouAEIOU'
    if simbolo in vogais:
        return True
    else:
        return False

def todos_sao_vogais(st):
    for i in range(len(st)):
        if vogal(st[i]) == False:
            return False
    return True

# PROGRAMA PRINCIPAL

print(vogal('*')) # False
print(vogal('A')) # True
print(vogal('V')) # False
print(vogal('e')) # True

print(todos_sao_vogais('aaaaaaaaaaaaaaa'))
print(todos_sao_vogais('aaaaaaaaPAROU'))
