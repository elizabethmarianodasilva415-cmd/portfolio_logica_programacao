import os
os.system('cls|| clear')

contador=0
acumulador=0

alunos_lista=[1,2,3,4,5]
for i in alunos_lista: 
    print(f"lista de valores: {i}")
    contador=contador+1
    acumulador = acumulador + i
  

print(f"Na sala tem: {contador} ")
print(f'na sala soma é:{acumulador}')