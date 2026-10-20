import os
os.system('cls')

def somar_com_print(a, b):
    print(a+b)

resultado = somar_com_print(3,2)
print(resultado)

def somar_com_return(a, b):
    return a + b

# 1. A variável "resultado" agora guarda o número 5 de verdade
resultado = somar_com_return(2, 3)

print(resultado)  # Mostra 10 na tela!