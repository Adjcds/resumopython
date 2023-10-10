# Dicionarios

# Criando dicionarios

dicionario = {}
dicionario = dict()

dicionario = { 'nome': 'Adrielle', 'idade': 26, 'altura': 1.78 }
print(dicionario)
#print(dicionario['idade'])

#adicionar elementos em um dicionario

dicionario['programador'] = True
print(dicionario)

dicionario['altura'] = 2 
# quando o valor ja existe ele sobre escreve


# Interando sobre um dicionario

for chave in dicionario:
 #print(chave)
 print(chave,':', dicionario[chave] )

# Testando a existencia de uma chave

print('peso' in dicionario)
print('altura' in dicionario)
