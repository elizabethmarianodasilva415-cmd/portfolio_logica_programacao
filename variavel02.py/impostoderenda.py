import os
os.system('cls|| clear')

salario =float(input("Digite seu salario\n"))
if (salario > 0) and(salario <=2.112):
    print("Você não paga imposto")
elif (salario >2.113) and (salario <= 2.826):
    print("Seu imposto é de 7,5% de imposto")
elif (salario > 2.827) and (salario <= 3.751):
    print("seu imposto é 15% de imposto")
elif (salario > 3.752) and (salario <= 4.664):
    print("Seu imposto é de 22,5%")
elif (salario > 4.665):
    print("Seu imposto é de 27.5")
    
dependentes = int(input("Digite quantos de dependentes\n"))
previdencia = int(input("Digite quanto de previdencia você paga\n"))
pensao = int(input("Digite o valor da pensão\n"))






