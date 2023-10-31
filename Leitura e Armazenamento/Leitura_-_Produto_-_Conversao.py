# - Resolva os exercícios usando a linguagem Python.
# 1. Construa o programa que leia dez números inteiros quaisquer e calcule o produto deles.
# Para facilitar os testes, resolva primeiro com dois números. Use for.

import random
produto = 1
for i in range(0,10+1):
    num_inteiro = random.randint((-100),(100))
    produto = produto * num_inteiro
    print(num_inteiro)
print("Produto: ", produto)

# 2. Construa o programa que leia “n” números inteiros quaisquer e calcule o produto deles. 
# O usuário fornecerá a quantidade de números, ou seja, o valor de “n”. 
# O usuário vai digitar também os “n” valores. Use o for. 

while True:
    vi = 1
    vf = int(input("Digite o valor final da quantidade de numeros a ser usada:"))
    produto_ = 1
    if vi < vf:
        for c in range(vi,vf+1):
            n = int(input("Digite um valor:"))
            produto_ = produto_ * n
        break
    elif vi == vf:
        print("os valores são iguais")
        continue
    else:
        for c in range(vi,vf-1,-1):
            n = int(input("Digite um valor:"))
            produto_ = produto_ * n
        break
print("Produto:",produto_)

#3. A conversão de graus Fahrenheit para graus Celsius é obtida pela fórmula abaixo. 
# Fórmula:	 c = 5 ( f - 32 )/9
# O usuário fornecerá os valores inicial e final de graus Fahrenheit. 
# Calcule a conversão e gere o relatório de saída tabular (em forma de tabela) considerando o intervalo digitado. 
# Gere o relatório na ordem crescente, se o valor inicial for menor ou igual ao valor final. 
# E na ordem decrescente, se valor inicial for maior que o valor final.

fi= int(input("Digite um valor do Fahrenheit inicial:"))
ff= int(input("Digite um valor do Fahrenheit final:"))
if fi < ff:
    print("︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵")
    print("     Fahrenheit para Celsius ")
    print("────♡- - - - - - - - - - - -♡─────")
    for z in range(fi,ff+1):
        celsius = (5*(z-32))/9
        def criarTabela():
            print(f"┊\t{z}F° = {celsius:.2f}°\t\t ┊")
        criarTabela()
    print("────♡- - - - - - - - - - - -♡─────")
    print("︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶")
else:
    print("︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵︵")
    print("     Fahrenheit para Celsius ")
    print("────♡- - - - - - - - - - - -♡─────")
    for z in range(fi,ff-1,-1):
        celsius = (5*(z-32))/9
        def criarTabela():
            print(f"┊\t{z}F° = {celsius:.2f}°\t\t ┊")
        criarTabela()
    print("────♡- - - - - - - - - - - -♡─────")
    print("︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶")