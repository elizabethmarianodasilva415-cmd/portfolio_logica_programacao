import os
os.system('cls|| clear')

nota1= float(input("Digite a 1° nota"))
nota2= float(input("Digite a 2° nota"))

media = (nota1+nota2)/2
    
if(media >= 7):
       print("Voce foi aprovado(a).\nSua media foi:", media)
elif (media >=4) and (media <= 6.9):
        print('Você foi aprovado(a), mas ficou de recuperaçõa por média.\nSua média foi:',media)
else:
       print('Você foi reprovado por média.\nSua média foi:', media)