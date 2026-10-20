import os
os.system('cls|| clear')

idade = int(input('Digite sua idade '))

if (idade >= 16):
    print('Você pode votar')
    if (idade >= 18):
        print('O voto é obrigatório!')
    else:
        print('O voto é facultativo!')
else:
    print('Você não pode votar ainda!')
    print(f'Faltam {16-idade} ano(s)')

