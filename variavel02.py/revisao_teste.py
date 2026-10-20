import os
os.system('cls || clear')

idade = int(input('Digite sua idade '))
media = float(input('Digite sua média '))

if (media >= 8.5):
    print('Excelência')
else:
    if (media >= 7):
        print('Satisfatório')
    else:
        if (media >= 5):
            print('Recuperação')
        else:
            if (media < 5):
                print('Reforço Intensivo') 

if (idade >= 11) and (idade <= 13):
    print('Ensino fundamental II')  
else:
    if (idade >= 14) and (idade <= 17):
        print('Ensino médio')
    else:
        if (idade >= 18):
            print('EJA (Educação de Jovens e Adultos)')
        else:
            print('Sem classificação')
       
        