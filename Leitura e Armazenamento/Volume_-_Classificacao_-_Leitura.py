# - Resolva os exercícios usando a linguagem Python.
# 1. Faça o programa que calcule o volume de uma esfera de raio R. 
# O usuário fornecerá o dado necessário.
# Onde:	 volume = 4/3 π r³   

operacao = int(input("Qual tipo de medida está seu raio:\n[1] Centímetros\n[2] Metros\n"))
if operacao > 0 and operacao < 3:
    if operacao == 1:
        import math
        π = math.pi
        r = float(input("Informe o raio da esfera: "))
        volume1 = (4/3) * π * (r ** 3)
        volume1_alterado = "{:.2f}".format(volume1)
        print("O volume da esfera aproximado é o total de: {}cm³".format(volume1_alterado))
    if operacao == 2:
        import math
        π = math.pi
        r = float(input("Informe o raio da esfera: "))
        volume2 = (4/3) * π * (r ** 3)
        volume2_alterado = "{:.2f}".format(volume2)
        print("O volume da esfera aproximado é o total de: {}m³".format(volume2_alterado))
else:
    print("Opção inválida.")

#2. Escreva o programa que classifique três valores inteiros quaisquer em ordem crescente. 
# Os valores serão fornecidos pelo usuário. 
# Resolva sem usar operador lógico (e, ou, não).

valor1 = int(input("Primeiro valor: "))
valor2 = int(input("Segundo valor: "))
valor3 = int(input("Terceiro valor: "))
if valor1 > valor2 > valor3:
    print("{}\n{}\n{}".format(valor3, valor2, valor1))
elif valor2 > valor1 > valor3:
    print("{}\n{}\n{}".format(valor3, valor1, valor2))
elif valor3 > valor2 > valor1:
    print("{}\n{}\n{}".format(valor1, valor2, valor3))
elif valor1 > valor3 > valor2:
    print("{}\n{}\n{}".format(valor2, valor3, valor1))
elif valor2 > valor3 > valor1:
    print("{}\n{}\n{}".format(valor1, valor3, valor2))
elif valor3 > valor1 > valor2:
    print("{}\n{}\n{}".format(valor2, valor1, valor3))
else:
    print("Existe Números iguais!")

#3. Desenvolva o programa que leia vários valores reais e no final mostre as seguintes informações:
#A quantidade de valores digitados;
#A soma dos valores digitados;
#A média aritmética dos valores digitados;
#A porcentagem dos valores maiores que dez digitados.
#Obs.: use o valor 0 (zero) como condição de saída da estrutura de repetição.

ct = 0
soma = 0
print("Digite 0 para finalizar o programa.")
while True:
    numero = float(input("Digite um número: "))
    if numero == 0:
        print("Programa finalizado.")
        break
    if numero != 0:
        soma = soma + numero
        ct = ct + 1
        media  = soma / ct
        resto = numero % 2
        print("A quantidade de dígitos é equivalente a: ", ct)
        print("A soma dos valores digitados é: ", soma)
        print("A média aritmética dos números é: % .2f" % (media))
        if numero > 10:
            resto = soma / 100
            print("A porcentagem dos valores maiores que 10 digitados é: ", resto)
 
 # Código de Luísa Amâncio Brambilla - Turma B - Matutino.
