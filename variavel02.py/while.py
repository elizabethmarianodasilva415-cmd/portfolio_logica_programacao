import os
os.system('cls|| clear')

mensagem = str(input('Digite sua mensagem (digite "sair" para finalizar o chat): '))
print(f'Você escreveu: {mensagem}').lower()

while (mensagem != 'sair'):
    mensagem = str(input('Digite sua mensagem (digite "sair" para finalizar o chat): '))
    print(f'Você escreveu: {mensagem}')

print('FIM')