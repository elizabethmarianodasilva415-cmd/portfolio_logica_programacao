import os
os.system('cls|| clear')

print("promoção!")
print("pagamento no pix ganham 10% de desconto!\n")

nome = str(input("qual é o seu nome?\n"))
produto = str(input("qual é o seu produto?\n"))
quantidade = int(input("quantas unidades você possui\n"))
preco = float(input("qual é o valor do produto?\n"))
pagamento = str(input("qual será a forma de pagamento?\n"))
if pagamento == "pix":
     print('seu desconto é de 10%')
     total = 0.90 * (quantidade * preco)
else: 
    total = (quantidade * preco)
print("seus produtos deram;\n", total)

resposta =input("deseja finalizar a compra\n")
if resposta == "sim":
    print("resumo da sua compra:")
    print("seu nome é\n", nome)
    print("o produto selecionado foi\n", produto)
    print("quantidade selecionada: \n", quantidade)
    print("o valor total da sua compra: \n", total)
    print("obrigado por sua preferencia")
    