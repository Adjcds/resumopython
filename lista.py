# > Listas
#indice (posição)
#antes

nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

#com listas
notas = {7.9, 9.7, 8.2}

#criar listas 
listas = {}
listas = list()
lista = [26, 'adrielle', 3.14459, False]
lista_de_listas = [10, [ 1, 2, 3]]

#idexação e slices (fatiamento)

lista = [10, 'Adrielle', 3.1415, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
#print(lista[4])

print(lista[-1]) #-1 é o ultimo elemento, -2 o pentmo...

#slices

lista = [10, 50, 30, 40, 25, 60 ,5]

print(lista[0:3]) #> começa no indice 0 e vai ate menor do que menos 3       10, 50, 30
print(lista[3:6]) #> Menor do que o indice 6, então o indice 6 não está incluso   40, 25, 60
print(lista[3:]) #ele vai até o final
print(lista[2:6:2]) #pular de dois em dois    pois comeca contando no 2 até o 6, porém o terceiro numero o 2 e a quantidade de vezes que deve pular

# > Interações com FOR

# 1. Ultilizando os próprios elementos da lista

for elemento in lista:
  print(elemento)

# 2. ultilizando os indices
#len tras a quantidade de elementos que existem
print('comprimento da lista:', len(lista))

for i in range(len(lista)):
  print(lista[i])


#metodos de lista

lista =[1, 3, 12, 8, 2]

#append (adicionando no final da lista)

print('antes do append;', lista)

lista.append(3)

print('depois do append:', lista)

#insert (adiciona o elemento escolhe a posição)

lista.insert(2, 10)

print('depois do insert;', lista)

#extend (juntar duas listas)

lista2 = [1, 2, 3]

lista.extend(lista2)

print('depois do extend:', lista)

#pop (para remover o elemento que vc expecificou ou se vc não escolher, ele vai remover o ultimo)

lista.pop()

print('lista apos o pop:', lista)

lista.pop(0) 
print('lista apos o pop:', lista)

#remove (não é o indice, é o elemento qual deseja remover)

lista.remove(3)
print('lista depois do remove:', lista) #ele elemina o primeiro que ele encontra

#count (quando vc quer contar quantas vezes um elemento aparece na sua lista)

print('quantidade de 2 na lista:', lista.count(2))

#index (ele te diz o indice de um determinado elemento dentro da lista)

print('indice do elemento 12:', lista.index(12))

#sort (ele serve para vc ordenar a sua lista)
 
lista.sort() #(reverse=True) ordena descrecente 
print('sort:', lista)

#Funções de listas

#len (saber quantos elementos tenho na lista)

print(len(lista))

#sum (somar tds os elementos da lista )

print(sum(lista))

#max

print('maior elemento da lista:', max(lista))

#min
print('menor elemento da lista:', min(lista))
