import os
os.system('cls')

notas=[7.5,8.0,9.0]

for i in range(len(notas)):
    print(notas[i])
    
soma = sum(notas)
media = sum(notas)/ len(notas)
print(f'A média é {media}')