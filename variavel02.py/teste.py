import os
os.system('cls|| clear')
 
compras = float(input("bem vindo!\ndigite o valor da sua compra:\n"))
if(compras >= 300):
    print("Você ganhou um desconto de 15%!")
    desconto = 0.15
elif (compras >=200):
    print("você ganhou um desconto de 12%!")
    desconto = 0.12
else:
    desconto = 0.10
    
modulo = (compras * desconto)
total = compras - modulo 
print(f"resumo da sua compra\nseu desconto foi de {modulo}\no total da sua compra foi de {total}")