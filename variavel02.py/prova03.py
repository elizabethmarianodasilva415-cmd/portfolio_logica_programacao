import os
os.system('cls|| clear')


print('Digite sua idade')
idade = int(input())
if (idade >= 0) and (idade <= 16):
  print('Você pode entrar')
if (idade >= 16) and (idade <= 17):
  print('Você precisa de um reponsavel para te acompanhar ')
if (idade >= 18):
    print("Você é adulto")
