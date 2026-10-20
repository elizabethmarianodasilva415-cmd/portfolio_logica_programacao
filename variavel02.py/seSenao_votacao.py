import os
os.system('cls|| clear')

print("Digite sua idade:")
idade = int(input())

if idade >= 16:
    print("Você pode votar!")
    if idade >= 18:
        print("Voto obrigatório")
    else:
        print("Voto facultativo")
        
else:
    print("Voto ainda não pode votar!")
    print("Faltam" , 16 - idade,"anos")
