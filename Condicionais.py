#estruturas condicionais
#':' então
idade = int(input())

if idade >= 18:
  print('você é maior de idade.')   
else: 
  print('você é menor de idade.')


'''
Imagine que você queira imprimir 'aprovado(a)', no caso o estudante 
tem uma media superior ou igual a 7, e 'reprovado', caso a media seja inferior a 7
'''

'''media = float(input( 'informe a media do estudante:' ))

if media >= 7:
  print('aprovado(a)')
elif media >= 5:
  print('recuperação')
else:
  print('reprovado(a)')'''

media = int(input())
presenca = int(input())

if media >= 7 and presenca >= 70:
  print('Você foi aprovado:)')
  print('Parabéns')
else: 
  print('Você foi reprovado:(')
  print('Tente novamente')

