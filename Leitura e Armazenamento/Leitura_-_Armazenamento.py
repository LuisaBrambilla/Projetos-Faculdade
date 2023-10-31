# - Exercícios:
# 1- Desenvolva o programa que faça a leitura de vários números digitados pelo
# usuário e use o valor -1 como condição (flag) de saída da estrutura de repetição.
# Na tela de saída, mostre a quantidade de números digitados.
# Obs.: resolva sem usar lista.

ct = 0
print("Digite [-1] para sair do programa.")
while True:
    numero = int(input("Número: "))
    if numero == -1:
        print("Você saiu do programa.")
        break
    else:
        ct += 1
print("A quantidade de números digitados é equivalente à: ", ct)

# 2- Desenvolva o programa que faça a leitura de vários números digitados pelo
# usuário e use o valor -1 como condição (flag) de saída da estrutura de repetição.
# Na tela de saída, mostre a quantidade de números digitados.
# Obs.: resolva usando lista.

lista = []
print("Digite [-1] para sair do programana.")
while True:
    valor = int(input("Número: "))
    if valor == -1:
        break
    lista.append(valor)
print("Quantidade de números digitados:", len(lista))

# 3- Desenvolva o programa que leia vários números, armazene-os numa lista e mostre
# estas informações:
# a- Quantidade de elementos armazenados na lista;
# b- Soma dos valores da lista;
# c- Maior valor da lista;
# d- Menor valor da lista;
# e- Produto dos números;
# f- Crie o enunciado e a resposta de mais um item de exercício;
# g- Crie o enunciado e a resposta de mais um item de exercício;

import statistics 
from math import prod
lista = []
print("Digite [-1] pra sair.")
while True:
    valor = int(input("Valor: "))
    if valor == -1:
        break
    lista.append(valor)
print("Quantidade de elementos armazenados na lista: ", len(lista))
print("Soma dos valores da lista: ", sum(lista))
print("Maior valor da lista: ", max(lista))
print("Menor valor da lista: ", min(lista))
print("Produto dos números: ", prod(lista))
# f- Mostre em ordem crescente os valores dentro da lista.
lista.sort()
print("Ordem crescente: ", lista)
# g- Mostre a média dos valores.
media = statistics.mean(lista)
print('Média:', media)

# Código de Luísa Amâncio Brambilla - Turma B - Matutino.