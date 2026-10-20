import os
os.system('cls')

# O que está dentro da função é o escopo da função
def terra():
    print('olá, somos da terra')

# o que está fora de funções é o escopo global
print('Somos da água')

terra()