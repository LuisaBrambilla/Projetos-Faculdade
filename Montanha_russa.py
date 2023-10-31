import threading
import time
import random

# Parâmetros do problema

## Passageiros
n = int(input("Digite o numero de passageiros que vão entrar na fila: "))  # Número total de passageiros
s = n # Numero inalteravel de total dos passageiros
p = 0  # Embarque dos passageiros
passageiro = 0  # Passageiro em espera
ct = 0  # Contagem para ID dos passageiros
idP = []  # Lista de ID dos passageiros
Tp1 = int(input("Digite o primeiro tempo de chegada entre passageiros: "))
Tp2 = int(input("Digite o segundo tempo de chegada entre passageiros: "))

## Carrinhos
m = int(input("Digite a quantidade de carrinhos: "))  # Número total de carros
C = int(input("Digite a capacidade do carrinho: "))  # Capacidade de cada carro
idC = []  # ID dos carros
mId = 0  # Variavel de criação dos ID dos carros
for i in range(m):  # Cria o ID dos carros
  mId += 1
  idC.append(mId)
fila2 = []  # Fila de carros em espera
Te = int(input("Digite o tempo de embarque/desembarque: "))  # Tempo de embarque/desembarque (em segundos)
Tm = int(input("Digite o tempo de duração do passeio: "))  # Tempo de passeio (em segundos)
tmt = 0 # Tempo total de passeio
x = 0  # Carro que terminou o passeio
oc = 0  # Carros ocupados
ol = m  # Carros livres

# Semáforo
mutex = threading.Semaphore(1)
k = 0 # Filtro do timer

# Timer
tmr = 0
cdinicio = time.time()
def timer():
  global tmr
  while n > 0:
    tmr += 1
    time.sleep(1)




# Print dos dados iniciais:
print(
    f"----------------------------------------\nNúmero de passageiros: {n}\nNúmero de carros: {m}\nCapacidade do carro: {C}\n----------------------------------------"
)


# Chegada de passageiros
def ChegaPassageiro():
  global passageiro, n, idP, ct
  for _ in range(n):
    passageiro += 1
    ct += 1
    idP.append(ct)
    print(f"{tmr} - Passageiro {idP[ct - 1]} chegou.")
    time.sleep(random.uniform(Tp1, Tp2))


# Embarque no carrinho
def Embarque():
  global passageiro, m, n, p, idP, idC, oc, fila2, C, s
  while n > 0:
    if passageiro < C and ct == s and m != 0 and len(
        idC) != 0 and passageiro > 0:
      print(
          f"Carro {idC[0]} começou o embarque de {passageiro} passageiros.\n")
      fila2.append(idC[0])
      idC.pop(0)
      passageiro -= passageiro
      time.sleep(5)
      print(f"\n{tmr} - Embarque feito.\n")
      m -= 1
      p += 1
    else:
      if passageiro >= C and m != 0 and len(idC) != 0:
        print(
            f"\n{tmr} - Carro {idC[0]} começou o embarque de {C} passageiros.\n"
        )
        fila2.append(idC[0])
        idC.pop(0)
        passageiro -= C
        time.sleep(5)
        print(f"\n{tmr} - Embarque feito.\n")
        m -= 1
        p += 1


# Passeio do carrinho
def Passeio():
  global passageiro, m, n, p, x, idP, idC, fila2, Tm, tmt
  while n > 0:
    if p != 0:
      mutex.acquire()
      print(
          f"\n{tmr} - Passeio do carro {fila2[0]} começando, apertem os cintos.\n"
      )
      time.sleep(Tm)
      print(
          f'\n{tmr} - O carro {fila2[0]} voltou e os passageiros estão desembarcando...\n'
      )
      x += 1
      p -= 1
      tmt += Tm
      mutex.release()
      Desembarque_thread = threading.Thread(target=Desembarque)
      Desembarque_thread.start()

# Desenbarque do carrinho (Após passeio)
def Desembarque():
  global passageiro, m, n, p, x, idP, idC, C_Livre, fila2, C
  if x != 0:
    mutex.acquire()
    time.sleep(5)
    n -= C
    print(f"\n{tmr} - Desembarque do carro {fila2[0]} feito.\n")
    idC.append(fila2[0])
    fila2.pop(0)
    m += 1
    x -= 1
    mutex.release()

# Controle de tempo/Relatorio
def tempo():
  global passageiro, ct, s, k, C, Tm
  while n > 0:
    if k == 0:
      inicio = time.time()
      k = 1
    if ct == 1 and k == 1:
      inicio_primeiro = time.time()
      k = 2
    elif ct == C and k == 2:
      final_primeiro = time.time()
      k = 3
    elif ct == s and k == 3:
      inicio_ultimo = time.time()
      k = 4
    elif passageiro == 0 and k == 4:
      final_ultimo = time.time()
  final = time.time()
  time.sleep(2)
  print("----------------------------------------")
  print("Relatorio de programa: ")
  print(f"Tempo minimo de espera: {round(final_primeiro - inicio_primeiro)}")
  print(f"Tempo maximo de espera: {round(final_ultimo - inicio_ultimo)}")
  print(
      f"Tempo medio de espera: {round(((final_primeiro - inicio_primeiro) + (final_ultimo - inicio_ultimo))/2)}"
  )
  print(f"Eficiencia: {round(((tmt/(final - inicio))*100))}%")
  print("----------------------------------------")

ChegaPassageiro_thread = threading.Thread(target=ChegaPassageiro)
ChegaPassageiro_thread.start()
Embarque_thread = threading.Thread(target=Embarque)
Embarque_thread.start()
Passeio_thread = threading.Thread(target=Passeio)
Passeio_thread.start()
tempo_thread = threading.Thread(target=tempo)
tempo_thread.start()
timer_thread = threading.Thread(target=timer)
timer_thread.start()