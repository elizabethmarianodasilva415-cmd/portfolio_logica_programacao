import os
os.system('cls|| clear')

idade = int(input("Digite sua idade:"))
peso = float(input("Digite seu peso:"))
 
if(idade >=18) and (idade <= 69) and (peso > 50):
    print("Você está elegivel para doar sangue")
else:
    print("Você está inelegivel para doar sangue")
