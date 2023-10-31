# - Resolva os exercícios usando a linguagem Python e os conceitos de POO (Programação Orientada a Objetos):

# 1. Crie uma classe com o método construtor e pelo menos três atributos. 
# E use pelo menos dois atributos com valor default (padrão).

class Gatos:
    def __init__(self, nome, idade, signo):
        self.nome = nome
        self.idade = idade
        self.signo = signo
    def get_nome(self):
        return self.nome
    def get_idade(self):
        return self.idade
    def get_signo(self):
        return self.signo
if __name__ == '__main__':
    gato1 = Gatos("Luna", 2, "Sargitário")
    gato2 = Gatos("Mion", 2, "Libra")
    print("- Gato 1: -")
    print(f"Código do objeto: {gato1}")
    print("Nome:", gato1.get_nome())
    print("Idade:", gato1.get_idade())
    print("Signo:", gato1.get_signo())
    print("- Gato 2 -")
    print(f"Código do objeto: {gato2}")
    print("Nome:", gato2.get_nome())
    print("Idade:", gato2.get_idade())
    print("Signo:", gato2.get_signo())

# 2. Crie os métodos gets e sets dos atributos.

class Gatos:
    def __init__(self, nome, idade, signo):
        self.nome = nome
        self.idade = idade
        self.signo = signo
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_idade(self):
        return self.idade
    def set_idade(self, nova_idade):
        self.idade = nova_idade
    def get_signo(self):
        return self.signo
    def set_signo(self, novo_signo):
        self.signo = novo_signo
if __name__ == '__main__':
    gato1 = Gatos("Luna", 2, "Sargitário")
    gato2 = Gatos("Mion", 2, "Libra")
    print("- Gato 1: -")
    print(f"Código do objeto: {gato1}")
    print("Nome:", gato1.get_nome())
    print("Idade:", gato1.get_idade())
    print("Signo:", gato1.get_signo())
    print("- Gato 2 -")
    print(f"Código do objeto: {gato2}")
    print("Nome:", gato2.get_nome())
    print("Idade:", gato2.get_idade())
    print("Signo:", gato2.get_signo())
    nome1 = input("Novo nome: ")
    gato1.set_nome(nome1)
    print("Nome atualizado: ", gato1.get_nome())
    idade2 = input("Nova idade: ")
    gato2.set_idade(idade2)
    print("Idade atualizada: ", gato2.get_idade())

# 3. Faça pelo menos uma crítica (validação) nos métodos sets.

class Gatos:
    def __init__(self, nome, idade, signo):
        self.nome = nome
        self.idade = idade
        self.signo = signo
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_idade(self):
        return self.idade
    def set_idade(self, nova_idade):
        if self.idade <= 0:
            print("Idade inváida.")
        self.idade = nova_idade
    def get_signo(self):
        return self.signo
    def set_signo(self, novo_signo):
        self.signo = novo_signo
if __name__ == '__main__':
    gato1 = Gatos("Luna", 2, "Sargitário")
    gato2 = Gatos("Mion", 2, "Libra")
    print("- Gato 1: -")
    print(f"Código do objeto: {gato1}")
    print("Nome:", gato1.get_nome())
    print("Idade:", gato1.get_idade())
    print("Signo:", gato1.get_signo())
    print("- Gato 2 -")
    print(f"Código do objeto: {gato2}")
    print("Nome:", gato2.get_nome())
    print("Idade:", gato2.get_idade())
    print("Signo:", gato2.get_signo())
    nome1 = input("Novo nome: ")
    gato1.set_nome(nome1)
    print("Nome atualizado: ", gato1.get_nome())
    idade2 = input("Nova idade: ")
    gato2.set_idade(idade2)
    print("Idade atualizada: ", gato2.get_idade())

# 4. Crie pelo menos dois métodos funcional, ou seja, mais dois métodos além dos métodos gets e sets.

class Gatos:
    def __init__(self, nome, idade, signo):
        self.nome = nome
        self.idade = idade
        self.signo = signo
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_idade(self):
        return self.idade
    def set_idade(self, nova_idade):
        self.idade = nova_idade
    def get_signo(self):
        return self.signo
    def set_signo(self, novo_signo):
        self.signo = novo_signo
    def retorna_dados(self):
        dados = f"{self.get_nome()}, {self.get_idade()}, {self.get_signo()}"
        return dados
    def mostra_dados(self):
        print("Idade:", self.nome)
        print("Idade:", self.idade)
        print("Signo:", self.signo)
if __name__ == '__main__':
    gato1 = Gatos("Luna", 2, "Sargitário")
    gato2 = Gatos("Mion", 2, "Libra")
    print("- Gato 1: -")
    print(f"Código do objeto: {gato1}")
    print("Nome:", gato1.get_nome())
    print("Idade:", gato1.get_idade())
    print("Signo:", gato1.get_signo())
    print("- Gato 2 -")
    print(f"Código do objeto: {gato2}")
    print("Nome:", gato2.get_nome())
    print("Idade:", gato2.get_idade())
    print("Signo:", gato2.get_signo())
    nome1 = input("Novo nome: ")
    gato1.set_nome(nome1)
    print("Nome atualizado: ", gato1.get_nome())
    idade2 = input("Nova idade: ")
    gato2.set_idade(idade2)
    print("Idade atualizada: ", gato2.get_idade())
    print('Dados concatenados do gato 1:\n', gato1.retorna_dados())
    print('Dados concatenados do gato 2:\n', gato2.retorna_dados())
    gato1.mostra_dados()
    gato2.mostra_dados()

# 5. No método main, teste (use) a classe criada, crie pelo menos três objetos dessa classe, um objeto passando três argumentos, um objeto passando dois argumentos e um objeto passando um argumento.

class Gatos:
    def __init__(self, nome, idade=7, signo='libra'):
        self.nome = nome
        self.idade = idade
        self.signo = signo
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_idade(self):
        return self.idade
    def set_idade(self, nova_idade):
        self.idade = nova_idade
    def get_signo(self):
        return self.signo
    def set_signo(self, novo_signo):
        self.signo = novo_signo
    def retorna_dados(self):
        dados = f"{self.get_nome()}, {self.get_idade()}, {self.get_signo()}"
        return dados
    def mostra_dados(self):
        print("Idade:", self.nome)
        print("Idade:", self.idade)
        print("Signo:", self.signo)
if __name__ == '__main__':
    gato1 = Gatos("Luna", 2, "Sargitário")
    gato2 = Gatos("Mion", 2)
    gato3 = Gatos("Pepeu")
    print("- Gato 1: -")
    print(f"Código do objeto: {gato1}")
    print("Nome:", gato1.get_nome())
    print("Idade:", gato1.get_idade())
    print("Signo:", gato1.get_signo())
    print("- Gato 2 -")
    print(f"Código do objeto: {gato2}")
    print("Nome:", gato2.get_nome())
    print("Idade:", gato2.get_idade())
    print("- Gato 3 -")
    print(f"Código do objeto: {gato3}")
    print("Nome:", gato3.get_nome())
    nome1 = input("Novo nome: ")
    gato1.set_nome(nome1)
    print("Nome atualizado: ", gato1.get_nome())
    idade2 = input("Nova idade: ")
    gato2.set_idade(idade2)
    print("Idade atualizada: ", gato2.get_idade())
    print('Dados concatenados do gato 1:\n', gato1.retorna_dados())
    print('Dados concatenados do gato 2:\n', gato2.retorna_dados())
    print('Dados concatenados do gato 3:\n', gato3.retorna_dados())
    gato1.mostra_dados()
    gato2.mostra_dados()
    gato3.mostra_dados()

# 6. E teste (use) todos os métodos desenvolvidos na classe.

class Gatos:
    def __init__(self, nome, idade, signo):
        self.nome = nome
        self.idade = idade
        self.signo = signo
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_idade(self):
        return self.idade
    def set_idade(self, nova_idade):
        self.idade = nova_idade
    def get_signo(self):
        return self.signo
    def set_signo(self, novo_signo):
        self.signo = novo_signo
    def retorna_dados(self):
        dados = f"{self.get_nome()}, {self.get_idade()}, {self.get_signo()}"
        return dados
    def mostra_dados(self):
        print("Idade:", self.nome)
        print("Idade:", self.idade)
        print("Signo:", self.signo)
if __name__ == '__main__':
    gato1 = Gatos("Luna", 2, "Sargitário")
    gato2 = Gatos("Mion", 2, "Libra")
    gato3 = Gatos("Pepeu", 1, "Touro")
    print("- Gato 1: -")
    print(f"Código do objeto: {gato1}")
    print("Nome:", gato1.get_nome())
    print("Idade:", gato1.get_idade())
    print("Signo:", gato1.get_signo())
    print("- Gato 2 -")
    print(f"Código do objeto: {gato2}")
    print("Nome:", gato2.get_nome())
    print("Idade:", gato2.get_idade())
    print("Signo:", gato2.get_signo())
    print("- Gato 3 -")
    print(f"Código do objeto: {gato3}")
    print("Nome:", gato2.get_nome())
    print("Idade:", gato2.get_idade())
    print("Signo:", gato2.get_signo())
    nome1 = input("Novo nome: ")
    gato1.set_nome(nome1)
    print("Nome atualizado: ", gato1.get_nome())
    idade2 = input("Nova idade: ")
    gato2.set_idade(idade2)
    print("Idade atualizada: ", gato2.get_idade())
    print('Dados concatenados do gato 1:\n', gato1.retorna_dados())
    print('Dados concatenados do gato 2:\n', gato2.retorna_dados())
    print('Dados concatenados do gato 3:\n', gato3.retorna_dados())
    gato1.mostra_dados()
    gato2.mostra_dados()
    gato3.mostra_dados()

# Código de Luísa Amâncio Brambilla - Turma B - Matutino.