import os
os.system('cls|| clear')


print('Digite sua idade')
idade = int(input())
if (idade >= 0) and (idade <= 12):
  print('Você é uma criança')
if (idade >= 13) and (idade <= 17):
  print('Você é um adolescente')
if (idade >= 18) and (idade <= 64):
  print('Você é um adulto')
if (idade > 65):
  print('Você é um idoso')
