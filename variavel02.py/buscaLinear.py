
import os
os.system('cls')

codigos = [1061,1023,1024,1028,1027,1022,1020,1034,1065]

codigoProcurado = 1034

for i in range(len(codigos)):
    if codigoProcurado == codigos[i]:
        print(f'O código está na {i+1}º posição')

