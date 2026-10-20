Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 06/04/2026
Var
// Seção de Declarações das variáveis 
nota1, nota2, nota3, media, frequencia: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Didite a 1° nota")

leia(nota1)
escreval("Didite a 2° nota")
leia(nota2)
escreval("Didite a 3° nota")
leia(nota3)
escreval("Digite a frequencia")
leia(frequencia)

se (frequencia >= 75) entao
  media := (nota1 + nota2 + nota3) /3
  se (media >=7) entao
    escreval("Voce foi aprovado, com média:", media
  senao
   se (media >=4) e (media <=6.9) entao
      escreval("Voce ficou de recuperação, com média", media)
  senao
   escreval("Voce foi reprovado com média:", media)
   fimse
   fimse
senao
   escreval("Voce foi reprovado direto!")
fimse
   
  
  
Fimalgoritmo
