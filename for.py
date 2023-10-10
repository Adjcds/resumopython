#for (para) dentro  range(faixa)

# 0 1 2 3 4
'''for variavel in range(10):
  print(variavel)'''

# Menor do que o valor de parada 1 2 3 4 5 6 7 8 9 
'''for variavel in range(1, 10):
  print(variavel)'''

#1 4 7 10 valor de inicio, parada e valor passo(de quanto em quanto ele quer pular)
'''for variavel in range(1, 12, 3):
  print(variavel)'''

'''nota1 = float(input( 'informe sua nota 1:'))
nota2 = float(input( 'informe sua nota 2:'))
nota3 = float(input( 'informe sua nota 3:'))'''

soma = 0

for i in range(1, 4):
    nota = float(input(f'informe a sua nota {i}: ')) #f str com '{}'

    soma = soma + nota 

print(soma / 3) 
