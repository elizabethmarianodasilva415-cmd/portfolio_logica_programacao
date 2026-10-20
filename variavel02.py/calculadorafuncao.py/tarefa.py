import os
os.system('cls')

lista_tarefas= []

n1 = int(input('Digite o 1º número: '))
sinal = str(input('Digite o sinal da operação'))
n2 = int(input('Digite o 2º número: '))

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
                                                                                                                                                                                                                                                                                        
import os
import time
from tarefa import lista_tarefas, criar_tarefa, listar_tarefa, atualizar_tarefa, apagar_tarefa
os.system('cls')
  
def executar_menu():
    while True:
        time.sleep(2)
        print('\n---------Menu Principal---------')
        print('1. Criar Tarefa')
        print('2. Listar Tarefa(s)')
        print('3. Atualizar Tarefa')
        print('4. Apagar Tarefa')
        print('5. Sair')

        opcao = int(input('Escolha uma opção: '))

        if (opcao == 5):
            print('Programa Encerrado. Tchau!')
            break
        elif (opcao == 1):
            nome = str(input('Digite o nome da tarefa: '))
            criar_tarefa(nome)
        elif (opcao == 2):
            listar_tarefa()
        elif (opcao == 3):
            numero_tarefa = int(input('Digite o número da tarefa que será atualizada como "concluída"'))
            atualizar_tarefa(numero_tarefa)
        elif (opcao == 4):
            numero_tarefa = int(input('Digite o número da tarefa que será apagada'))
            apagar_tarefa(numero_tarefa)
            
executar_menu()
    
