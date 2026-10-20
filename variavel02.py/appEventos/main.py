from tarefas import tarefas
import os
os.system('cls')

while True:
    print("\n --- Lista de Tarefas ---")
    print('1 - Adicionar Tarefas')
    print('2 - Listar Tarefas')
    print('3 - Sair')

    opcao = int(input('Digite a opção desejada: '))

    if (opcao == 1):
        print('Opção para adicionar uma tarefa!')
    elif (opcao == 2):
        print('Opção para listar tarefas!')
    elif (opcao == 3):
        print('Programa encerrado!')
        break
    else:
        print('Número inválido')







