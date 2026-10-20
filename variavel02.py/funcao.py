import os
os.system('cls')

n1 = int(input('Digite o 1º número: '))
sinal = str(input('Digite o sinal da operação'))
n2 = int(input('Digite o 2º número: '))

# Criação de funções para cada operação:
def soma():
    print(f'{n1} + {n2} = {n1+n2}')
def subtracao():
    print(f'{n1} - {n2} = {n1-n2}')
def multiplicacao():
    print(f'{n1} x {n2} = {n1*n2}')
def divisao():
     print(f'{n1} / {n2} = {n1/n2}')
#  crie as outras 2 funções
if (sinal == '+'):
    soma()
if(sinal == '-'):
    subtracao()
if (sinal == '*'):
    multiplicacao()
if (sinal == '/'):
    divisao()
#     print(f'{n1} + {n2} = {n1+n2}')
# elif (sinal == '-'):
#     print(f'{n1} - {n2} = {n1-n2}')
# elif (sinal == '*'):
#     print(f'{n1} x {n2} = {n1*n2}')
# else:
#     print(f'{n1} / {n2} = {n1/n2}')
