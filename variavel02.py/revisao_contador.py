import os #importando biblioteca OS
import random #importando biblioteca Random
os.system('cls') #limpar o terminal com o CLS

numeroSorteado = random.randint(1,10) # escolhe um número de 1 a 10 e guarda em numeroSorteado

chute = 0 # valor do chute (inicializando em 0)
contador = 0 # valor do contador (inicializando em 0)

while (chute != numeroSorteado): # enquanto o chute da pesoa for diferente 
    #do numero sorteado, o enquanto continuará rodando

    chute = int(input('Tente acertar o número, digite um valor de 0 a 10: ')) 
    #variável chute armazena um número int digitado pelo usuário
    if (chute == numeroSorteado): #verificar se o chute é igual ao numero sorteado
        print('Você acertou!') # mostra a mensagem "você acertou"
    else: # senão
        print('Você errou!') # mostra a mensagem "você errou"

    if (chute > numeroSorteado): #verificar se chute é maior que numeroSorteado
        print('Chute um número menor') # mostra a mensagem 'Chute um número menor'
    if (chute < numeroSorteado): # verificar se chute é menor que o numeroSorteado
        print('Chute um número maior') # mostra a mensagem 'Chute um número maior'
    # contador = contador + 1
    contador += 1 # Conta de 1 em 1 as tentativas


print(f'O número sorteado foi o {numeroSorteado}') # Mostra a mensagem O número sorteado foi o {numeroSorteado}
print(f'Você acertou em {contador} tentativas')

