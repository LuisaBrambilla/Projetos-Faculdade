def soma(x, y):
    return x + y
def subtrai(x, y):
    calculo = x - y
    return calculo
if __name__ == '__main__':
    v1 = int(input("Primeiro valor: "))
    v2 = int(input("Segundo valor: "))
    v3 = 3
    v4 = 5
    opcao = int(input("[1] Somar\n[2] Subtrair\nOpção: "))
    if opcao == 1:
        print('Soma:', soma(v1, v2))
        s1 = soma(v1, v2)
        s2 = soma(v3, v4)
        calculo = s1 + s2
        print(calculo)
    elif opcao == 2:
        print('Subtração:', subtrai(v1, v2))
    else:
        print("Opção inválida.")
