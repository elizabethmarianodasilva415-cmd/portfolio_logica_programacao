import os
os.system('cls')

# criando a lista candidatos
candidatos = ['Candidato 1','Candidato 2','Candidato 3','Candidato 4','Candidato 5','Candidato 6','Candidato 7','Candidato 8','Candidato 9','Candidato 10', ]

#lista de votos
votos = [0,0,0,0,0,0,0,0,0,0]

# for que vai rodar 50 vezes
for j in range(50):
    #pergunta o voto todas as vezes
    voto = str(input('Digite o candidato que você deseja votar (Candidato 1 a Candidato 10: )'))
    #roda 10 vezes
    for i in range(10):
        if (voto == candidatos[i]):#verifica cada posição da lista de 10 candidatos
            print(f'Você votou no candidato {i+1}\n')
            votos[i] += 1
            print(votos)








