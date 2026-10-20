import os
os.system('cls|| clear')

velocidade = 95
multa = 0.0

if velocidade > 80:
    multa = (velocidade - 80) * 5.50
    print("Multa de R$", multa)
else:
    print(" Fim do programa")
          
        