import os
os.system('cls|| clear')

matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

acumulador=0

for linha in range(3):
    for coluna in range(3):
         acumulador = acumulador + matriz[linha][coluna]
print(f'A soma de toda a matriz resultou em {acumulador}')

for coluna in range(3):
    acumulador = acumulador + matriz[0][coluna]

print(f'A soma da linha 1 é {acumulador}')
for coluna in range(3):
    acumulador = acumulador + matriz[1][coluna]

print(f'A soma da linha 2 é {acumulador}')

for coluna in range(3):
    acumulador = acumulador + matriz[2][coluna]

print(f'A soma da linha 3 é {acumulador}')


