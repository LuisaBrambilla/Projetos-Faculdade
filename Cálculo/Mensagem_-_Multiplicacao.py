# - Resolva os exercícios usando a linguagem Python.
# 1. Desenvolva uma função que recebe uma mensagem e um número, ela mostra a mensagem e o número e não retorna nada. 
# A função main chama a função passando os argumentos. 

def shoot(mensagem, numero):
    print("A mensagem é:", mensagem)
    print("Número: ", numero)
if __name__ == '__main__':
    mensagem = str(input("Insira uma mensagem: "))
    numero = float(input("Número: "))
    shoot(mensagem, numero)

#2. Implemente uma função que recebe dois valores e retorna a multiplicação deles. 
# A função main chama essa função duas vezes.

def multiplicacao():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    multiplicacao = x * y
    print("Valor da multiplicação: ", multiplicacao)
    return multiplicacao
if __name__ == '__main__':
    multiplicacao()
    multiplicacao()

