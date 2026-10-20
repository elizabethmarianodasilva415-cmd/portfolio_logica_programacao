import os
os.system('cls || clear')


def ler_vetor():
   nums = []#Cria uma lista vazia chamda 'nums'
   n = int(input("Quantos números? "))#armazena em 'n' quantos números existirão na lista
   for i in range(n):# For vai rodar a quantidade de númeeros que a lista terá
       valor = int(input("Digite um número: "))#Armazena em 'valor' o número digitado
       nums.append(valor)#Adiciona o número dito pelo usuário na lista nums 

def exibir_vetor(nums):
    print("Vetor:", nums)#Mostra a lista

def somar_vetor(nums):
    soma = 0
    for v in nums:
        soma += v
        return soma

def calcular_media_vetor(nums):
    soma=somar_vetor(nums)
    media = soma / len(nums)
    return media

def encontrar_maior_valor(nums):
    maior = nums[0]
    for v in nums:
        if v > maior:
            maior = v
    return maior

#Teste de Leitura de Dados
vetor_numero=ler_vetor()

# Teste exibição de vetor
exibir_vetor(vetor_numero)

# Teste soma do vetor
resultado_soma=(somar_vetor(vetor_numero))
print(resultado_soma)

#Teste calcular de média
resultado_media=calcular_media_vetor(vetor_numero)
print(resultado_media)

#Teste encontrar o maior valor
resultado_maior_vetor=encontrar_maior_valor(vetor_numero)
print(resultado_maior_vetor)

















