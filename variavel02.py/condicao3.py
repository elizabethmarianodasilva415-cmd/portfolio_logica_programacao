import os
os.system('cls|| clear')


atleta= True
nota = 8.5
renda = 1640
bolsa100 = (nota>=9 and renda<=2000)

bolsa50= (nota>=8 and renda<=3000) or atleta
print("O aluno é elegivelpara bolsa de 50%:", bolsa50)

print('O aluno é elegível para bolsa de 100%:', bolsa100)


# escreval('O aluno é elegível para bolsa de 100%:', bolsa100)
# se ((nota >= 9) e (renda <= 2000)) entao
#  escreval("Você ganhou uma bolsa de 100%")

