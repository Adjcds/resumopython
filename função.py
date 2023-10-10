# > Funções

# 1. O que são funções e pq utilizá-las?

# Funções que já utilizamos anteriormente...

#print() # - Imprimir uma mensagem (int, float, str) no console (terminal, cmd)
#input() # - Retorna um dado informado pelo usuário (entrada padrão) e pode receber uma stri
#len() # - Recebe uma lista e retorna o tamanho da lista 
#max() # - Recebe o maior valor de uma lita

# 2. Criação de funções

#Função inicial

def saudacao(): 
  print('Seja bem vindo(a)!')
  print('Olá, é um prazer ter você fazendo parte desse curso')

#Você cria ela e tem que chamar a função pelo nome que vc criou
#Se não ela não ira ser executada, vc so definiu a estrutura dela, mas vc não ta utilizando
#Como você faz para utilizar 

saudacao()


# Função com parêmetros

def saudacao(nome, curso): 
  print(f'Seja bem vindo(a), {nome} !')
  print(f'Olá, é um prazer ter você fazendo parte do curso de, {curso}')

saudacao('Adrielle', 'Python') 
# se vc não adicionar irá dar erro (curso)

# Função com parâmetros default

def saudacao(nome, curso=' Python'): 
  print(f'Seja bem vindo(a), {nome} !')
  print(f'Olá, é um prazer ter você fazendo parte do curso de, {curso}')

saudacao('Adrielle', 'C++') 
# se vc não adicionar o valor padrão, ele vai assumir o valor dele padrão que é python


# Função com retorno

def soma(num1, num2):
  return num1 + num2
# so use o return no final da função, pq dali nada mais irá funcionar

resultado = soma(5, 7)

print( 'O Resultado da soma é:', resultado)

def calculadora(num1, num2, operacao='+'):
  if operacao == '+':
    return num1 + num2
  elif operacao == '-':
    return num1 - num2
  
resultado = calculadora(10, 20)

print(resultado)
