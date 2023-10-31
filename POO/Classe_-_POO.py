# - Exercícios:
# 1. Crie uma classe com o método construtor e pelo menos dois atributos.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def get_nome(self):
        return self.nome
    def get_idade(self):
        return self.idade
if __name__ == '__main__':
    pessoa1 = Pessoa('Luísa', 19)
    pessoa2 = Pessoa('Maurício', 28)
    print("- Pessoa 1: -")
    print(f"Código do objeto: {pessoa1}")
    print("Nome:", pessoa1.get_nome())
    print("Idade:", pessoa1.get_idade())
    print("- Pessoa 2 -")
    print(f"Código do objeto: {pessoa2}")
    print("Nome:", pessoa2.get_nome())
    print("Idade:", pessoa2.get_idade())

# 2. Crie os métodos gets e sets de todos os atributos.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_idade(self):
        return self.idade
    def set_idade(self, nova_idade):
        self.idade = nova_idade
if __name__ == '__main__':
    pessoa1 = Pessoa('Luísa', 19)
    pessoa2 = Pessoa('Maurício', 28)
    print("- Pessoa 1: -")
    print("Nome:", pessoa1.get_nome())
    print("Idade:", pessoa1.get_idade())
    print("- Pessoa 2 -")
    print("Nome:", pessoa2.get_nome())
    print("Idade:", pessoa2.get_idade())
    nome1 = input("Novo nome: ")
    pessoa1.set_nome(nome1)
    print("Nome atualizado: ", pessoa1.get_nome())
    idade2 = input("Nova idade: ")
    pessoa2.set_idade(idade2)
    print("Idade atualizada: ", pessoa2.get_idade())

# 3. No método main, teste (use) a classe criada, crie pelo menos três objetos dessa classe e use todos os métodos desenvolvidos na classe.

class Pessoa:
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
        dados = f'{self.get_nome()}, {self.get_idade()}, {self.get_signo()}'
        return dados
    def mostra_dados(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Signo:", self.signo)
    def mostra_dados2(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Signo:", self.signo)
if __name__ == '__main__':
    pessoa1 = Pessoa('Luísa', 19, 'Virgem')
    pessoa2 = Pessoa('Maurício', 28, 'Peixes')
    print("- Pessoa 1: -")
    print("Nome:", pessoa1.get_nome())
    print("Idade:", pessoa1.get_idade())
    print("Signo:", pessoa1.get_signo())
    print("- Pessoa 2 -")
    print("Nome:", pessoa2.get_nome())
    print("Idade:", pessoa2.get_idade())
    print("Signo:", pessoa2.get_signo())
    nome1 = input("Novo nome (Pessoa 1): ")
    pessoa1.set_nome(nome1)
    print("Nome atualizado: ", pessoa1.get_nome())
    idade2 = input("Nova idade (Pessoa 2): ")
    pessoa2.set_idade(idade2)
    print("Idade atualizada: ", pessoa2.get_idade())
    print('Dados associados da Pessoa 1:\n', pessoa1.retorna_dados())
    print('Dados associados da Pessoa 2:\n', pessoa2.retorna_dados())
    pessoa1.mostra_dados()
    pessoa2.mostra_dados()
    pessoa1.mostra_dados2()
    pessoa2.mostra_dados2()

#Código de Luísa Amâncio Brambilla - Turma B - Matutino.