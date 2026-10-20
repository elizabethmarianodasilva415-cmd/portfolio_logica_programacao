import os
os.system('cls')

loja = ['prateleira1', 'prateleira2', 'prateleira3', 'prateleira4', 'prateleira5']

prateleiras = ['produto1','produto2','produto3','produto4','produto5','produto6','produto7','produto8','produto9','produto10']

for prateleira in range(5):
    for produto in range(10):
        print(loja[prateleira], prateleiras[produto])