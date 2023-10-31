#- Exercícios:{
#1. Elabore o programa que calcula a área lateral de um cilindro.
# Onde:	área lateral= 2 π r h
# }

import math
π = math.pi
h = float(input("Digite o valor da altura: "))
r = float(input("Digite o valor do raio: "))
area_lateral_cilindro = 2 * π * r * h
area_lateral_cilindro_pi = 2 * r * h
area_lateral_cilindro_formatado1 = "{:.2f}".format(area_lateral_cilindro)
area_lateral_cilindro_formatado2 = "{:.2f}".format(area_lateral_cilindro_pi)
print("O valor da área lateral de um cilindro em cm² é: {}cm² ".format(area_lateral_cilindro_formatado1))
print("O valor da área lateral de um cilindro em πcm² é: {}πcm² ".format(area_lateral_cilindro_formatado2))

# 2. Elabore o programa que simule a calculadora com as quatro operações aritméticas básicas. 
# O usuário fornecerá dois números e a operação aritmética desejada. 
# Mostre o menu com estes símbolos (+ , - , * , / ) para o usuário escolher a operação aritmética.

operacao = int(input("Qual operação deseja realizar?\n[1] + Soma.\n[2] - Subtração.\n[3] * Multiplicação.\n[4] / Divisão.\n"))

if operacao > 0 and operacao < 5:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    if operacao == 1:
        resultado1 = numero1 + numero2
        print("O valor da operação será:", resultado1)
    if operacao == 2:
        resultado2 = numero1 - numero2
        print("Valor da operação é:", resultado2)
    if operacao == 3:
        resultado3 = numero1 * numero2
        print("Valor da operação é: % .2f" % (resultado3))
    if operacao == 4:
        if numero2 == 0:
            print("Não é possível realizar a divisão por zero.")
        else: 
            resultado4 = numero1 / numero2
            print("Valor da operação é: % .2f" % (resultado4))
else:
    print("Opção inválida.")

# Código de Luísa Amâncio Brambilla - Turma B - Matutino.

