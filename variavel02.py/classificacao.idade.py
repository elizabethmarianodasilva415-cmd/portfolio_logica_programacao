import os
os.system('cls|| clear')

idade = int(input("digite sua idade:\n"))

if idade <=12:
    print("você é uma criança \n entrada gratuito em cinemas!")
elif idade <=17:
    print("você é um adolescente \n meia entrada garantida!")
elif idade <=64:
    print("você é um adulto \n pode digirir e votar.")
elif idade >= 65:
    print("preferencia em filas!")