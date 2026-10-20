import os
os.system('cls|| clear')

nota1= float(input("Digite a 1° nota"))
nota2= float(input("Digite a 2° nota"))
nota3= float(input("Digite a 3° nota"))

frequencia = float(input("Coloque a frequencia do aluno"))
media = (nota1+nota2+nota3)/3
if (frequencia <= 75):
    print("Voce foi reprovado direto")
else:
   if(media >= 7):
       print("Voce foi aprovado(a) por frequência e media.\nSua media foi:", media)
   elif (media >=4) and (media <= 6.9):
        print('Você foi aprovado(a) por frequência, mas ficou de recuperaçõa por média.\nSua média foi:',media)
   else:
       print('Você foi reprovado por média.\nSua média foi:', media)