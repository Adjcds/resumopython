numero_sorteado = 15
numero_escolhido = int(input('informe um numero entre 1 e 20:'))
#while (enquanto)
#se a variavel do while não mudar pode acontecer o up infinito
while numero_sorteado != numero_escolhido: #ctrl + C interrompe o fluxo continuo de repetição
  print('Você errou o numero, tente novamente!')

  numero_escolhido = int(input('informe um numero entre 1 e 20:'))

print('Parabéns, você acertou eee! :) ')

#exemplo 02: Estrutura de Contador

contador = 0

while contador < 10:
  print(contador)

  contador = contador + 1
