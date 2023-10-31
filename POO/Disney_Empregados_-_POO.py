#- Resolva os exercícios usando a linguagem Python e os conceitos de POO (Programação Orientada a Objetos) com herança (inheritance):
# 1. Crie uma superclasse com o método construtor e pelo menos dois atributos. 
# Use pelo menos um atributo com valor default (padrão).

class Disney():
    def __init__(self, nome, cpf, salario, cargo='animador'):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.cargo = cargo

if __name__ == '__main__':
    tb1 = Disney('Rogério', '178.897.456-91', 17.000, 'Engenheiro')
    tb2 = Disney('Marcos', '785.443.289-26', 25.000)

# 2. Crie os métodos gets e sets dos atributos da superclasse.

class Disney():
    def __init__(self, nome, cpf, salario, cargo='animador'):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.cargo = cargo
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_cpf(self):
        return self.cpf
    def set_cpf(self, novo_cpf):
        self.cpf = novo_cpf
    def get_salario(self):
        return self.salario
    def set_salario(self, novo_salario):
        self.salario = novo_salario
    def get_cargo(self):
        return self.cargo
    def set_cargo(self, novo_cargo):
        self.cargo = novo_cargo

if __name__ == '__main__':
    tb1 = Disney('Rogério', '178.897.456-91', 17.000, 'Engenheiro')
    tb2 = Disney('Marcos', '785.443.289-26', 25.000)
    print(" ༘ Trabalhadorº 1:  ༘")
    print("  Nome:", tb1.get_nome())
    print("  CPF:", tb1.get_cpf())
    print("  Salário:", tb1.get_salario())
    print("  Cargo:", tb1.get_cargo())
    print("--------------------")
    print(" ༘ Trabalhadorº 2:  ༘")
    print("  Nome:", tb2.get_nome())
    print("  CPF:", tb2.get_cpf())
    print("  Salário:", tb2.get_salario())
    print("  Cargo:", tb2.get_cargo())

# 3. Faça pelo menos uma crítica (validação) em um dos métodos sets.

class Disney():
    def __init__(self, nome, cpf, salario=float, cargo='animador'):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.cargo = cargo
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_cpf(self):
        return self.cpf
    def set_cpf(self, novo_cpf):
        self.cpf = novo_cpf
    def get_salario(self):
        return self.salario
    def set_salario(self, novo_salario):
        if self.salario <= 0.0:
            print('Novo salário inválido!')
        self.salario = novo_salario
    def get_cargo(self):
        return self.cargo
    def set_cargo(self, novo_cargo):
        self.cargo = novo_cargo

if __name__ == '__main__':
    tb1 = Disney('Rogério', '178.897.456-91', 17.000, 'Engenheiro')
    tb2 = Disney('Marcos', '785.443.289-26', 25.000)
    print(" ༘ Trabalhadorº 1:  ༘")
    print("  Nome:", tb1.get_nome())
    print("  CPF:", tb1.get_cpf())
    print("  Salário:", tb1.get_salario())
    print("  Cargo:", tb1.get_cargo())
    print("--------------------")
    print(" ༘ Trabalhadorº 2:  ༘")
    print("  Nome:", tb2.get_nome())
    print("  CPF:", tb2.get_cpf())
    print("  Salário:", tb2.get_salario())
    print("  Cargo:", tb2.get_cargo())
    nvs = input('Digite o valor do novo salário: ')
    tb2.set_salario(nvs)
    print("Salário atualizado: ", tb2.get_salario())

# 4. Crie pelo menos um método funcional na superclasse, ou seja, mais um método além dos métodos gets e sets.

class Disney():
    def __init__(self, nome, cpf, salario=float, cargo='animador'):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.cargo = cargo
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_cpf(self):
        return self.cpf
    def set_cpf(self, novo_cpf):
        self.cpf = novo_cpf
    def get_salario(self):
        return self.salario
    def set_salario(self, novo_salario):
        if self.salario <= 0.0:
            print('Novo salário inválido!')
        self.salario = novo_salario
    def get_cargo(self):
        return self.cargo
    def set_cargo(self, novo_cargo):
        self.cargo = novo_cargo
    def retorna_dados(self):
        dados = f"Nome: {self.get_nome()}\nCPF: {self.get_cpf()}\nSalário: {self.get_salario()}\nCargo: {self.get_cargo()}"
        return dados

if __name__ == '__main__':
    tb1 = Disney('Rogério', '178.897.456-91', 17.000, 'Engenheiro')
    tb2 = Disney('Marcos', '785.443.289-26', 25.000)
    print(" ༘ Trabalhadorº 1:  ༘")
    print("  Nome:", tb1.get_nome())
    print("  CPF:", tb1.get_cpf())
    print("  Salário:", tb1.get_salario())
    print("  Cargo:", tb1.get_cargo())
    print('Dados concatenados do Trabalhador nº 1:\n', tb1.retorna_dados())
    print("--------------------")
    print(" ༘ Trabalhadorº 2:  ༘")
    print("  Nome:", tb2.get_nome())
    print("  CPF:", tb2.get_cpf())
    print("  Salário:", tb2.get_salario())
    print("  Cargo:", tb2.get_cargo())
    nvs = input('Digite o valor do novo salário: ')
    tb2.set_salario(nvs)
    print("Salário atualizado: ", tb2.get_salario())

# 5. Crie pelo menos duas subclasses com o método construtor e pelo menos três atributos.

class Disney():
    def __init__(self, nome, cpf, salario=float, cargo='animador'):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.cargo = cargo
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_cpf(self):
        return self.cpf
    def set_cpf(self, novo_cpf):
        self.cpf = novo_cpf
    def get_salario(self):
        return self.salario
    def set_salario(self, novo_salario):
        if self.salario <= 0.0:
            print('Novo salário inválido!')
        self.salario = novo_salario
    def get_cargo(self):
        return self.cargo
    def set_cargo(self, novo_cargo):
        self.cargo = novo_cargo
    def retorna_dados(self):
        dados = f"Nome: {self.get_nome()}\nCPF: {self.get_cpf()}\nSalário: {self.get_salario()}\nCargo: {self.get_cargo()}"
        return dados
class Diretor(Disney):
    def __init__(self, nome, cpf, tema):
        self.tema = tema
        super().__init__(nome, cpf)
class Personagens(Disney):
    def __init__(self, nome, desenho, cargo):
        self.desenho = desenho
        super().__init__(nome, cargo)

if __name__ == '__main__':
    tb1 = Disney('Rogério', '178.897.456-91', 17.000, 'Engenheiro')
    tb2 = Disney('Marcos', '785.443.289-26', 25.000)
    print(" ༘ Trabalhadorº 1:  ༘")
    print("  Nome:", tb1.get_nome())
    print("  CPF:", tb1.get_cpf())
    print("  Salário:", tb1.get_salario())
    print("  Cargo:", tb1.get_cargo())
    print('Dados concatenados do Trabalhador nº 1:\n', tb1.retorna_dados())
    print("--------------------")
    print(" ༘ Trabalhadorº 2:  ༘")
    print("  Nome:", tb2.get_nome())
    print("  CPF:", tb2.get_cpf())
    print("  Salário:", tb2.get_salario())
    print("  Cargo:", tb2.get_cargo())
    nvs = input('Digite o valor do novo salário: ')
    tb2.set_salario(nvs)
    print("Salário atualizado: ", tb2.get_salario())

# 6. Crie os métodos gets e sets dos atributos das subclasses.

class Disney():
    def __init__(self, nome, cpf, salario=float, cargo='animador'):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.cargo = cargo
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_cpf(self):
        return self.cpf
    def set_cpf(self, novo_cpf):
        self.cpf = novo_cpf
    def get_salario(self):
        return self.salario
    def set_salario(self, novo_salario):
        if self.salario <= 0.0:
            print('Novo salário inválido!')
        self.salario = novo_salario
    def get_cargo(self):
        return self.cargo
    def set_cargo(self, novo_cargo):
        self.cargo = novo_cargo
    def retorna_dados(self):
        dados = f"Nome: {self.get_nome()}\nCPF: {self.get_cpf()}\nSalário: {self.get_salario()}\nCargo: {self.get_cargo()}"
        return dados
class Diretor(Disney):
    def __init__(self, nome, cpf, tema):
        self.tema = tema
        super().__init__(nome, cpf)
    def get_tema(self):
        return self.tema
    def set_tema(self, novo_tema):
        self.tema = novo_tema
class Personagens(Disney):
    def __init__(self, nome, desenho, cargo):
        self.desenho = desenho
        super().__init__(nome, cargo)
    def get_desenho(self):
        return self.desenho
    def set_desenho(self, novo_desenho):
        self.desenho = novo_desenho

if __name__ == '__main__':
    tb1 = Disney('Rogério', '178.897.456-91', 17.000, 'Engenheiro')
    tb2 = Disney('Marcos', '785.443.289-26', 25.000)
    print(" ༘ Trabalhadorº 1:  ༘")
    print("  Nome:", tb1.get_nome())
    print("  CPF:", tb1.get_cpf())
    print("  Salário:", tb1.get_salario())
    print("  Cargo:", tb1.get_cargo())
    print('Dados concatenados do Trabalhador nº 1:\n', tb1.retorna_dados())
    print("--------------------")
    print(" ༘ Trabalhadorº 2:  ༘")
    print("  Nome:", tb2.get_nome())
    print("  CPF:", tb2.get_cpf())
    print("  Salário:", tb2.get_salario())
    print("  Cargo:", tb2.get_cargo())
    nvs = input('Digite o valor do novo salário: ')
    tb2.set_salario(nvs)
    print("Salário atualizado: ", tb2.get_salario())

# 7. No método main, teste (use) as classes criadas, crie pelo menos um objeto da superclasse, pelo menos dois objetos da primeira subclasse e pelo menos dois objetos da segunda subclasse.

class Disney():
    def __init__(self, nome, cpf, salario=float, cargo='animador'):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.cargo = cargo
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_cpf(self):
        return self.cpf
    def set_cpf(self, novo_cpf):
        self.cpf = novo_cpf
    def get_salario(self):
        return self.salario
    def set_salario(self, novo_salario):
        if self.salario <= 0.0:
            print('Novo salário inválido!')
        self.salario = novo_salario
    def get_cargo(self):
        return self.cargo
    def set_cargo(self, novo_cargo):
        self.cargo = novo_cargo
    def retorna_dados(self):
        dados = f"Nome: {self.get_nome()}\nCPF: {self.get_cpf()}\nSalário: {self.get_salario()}\nCargo: {self.get_cargo()}"
        return dados
class Diretor(Disney):
    def __init__(self, nome, cpf, tema):
        self.tema = tema
        super().__init__(nome, cpf)
    def get_tema(self):
        return self.tema
    def set_tema(self, novo_tema):
        self.tema = novo_tema
class Personagens(Disney):
    def __init__(self, nome, desenho, cargo):
        self.desenho = desenho
        super().__init__(nome, cargo)
    def get_desenho(self):
        return self.desenho
    def set_desenho(self, novo_desenho):
        self.desenho = novo_desenho

if __name__ == '__main__':
    tb1 = Disney('Rogério', '178.897.456-91', 17.000, 'Engenheiro')
    tb2 = Disney('Marcos', '785.443.289-26', 25.000)
    print(" ༘ Trabalhadorº 1:  ༘")
    print("  Nome:", tb1.get_nome())
    print("  CPF:", tb1.get_cpf())
    print("  Salário:", tb1.get_salario())
    print("  Cargo:", tb1.get_cargo())
    print('Dados concatenados do Trabalhador nº 1:\n', tb1.retorna_dados())
    print("--------------------")
    print(" ༘ Trabalhadorº 2:  ༘")
    print("  Nome:", tb2.get_nome())
    print("  CPF:", tb2.get_cpf())
    print("  Salário:", tb2.get_salario())
    print("  Cargo:", tb2.get_cargo())
    nvs = input('Digite o valor do novo salário: ')
    tb2.set_salario(nvs)
    print("Salário atualizado: ", tb2.get_salario())
    d1 = Diretor('Fábio', '785.449.234-89', 'Filmagem')
    d2 = Diretor('Leogis', '665.429.564-90', 'Luzes')
    p1 = Personagens('Mickey', 'A casa do Mickey Mouse', 'Protagonista')
    p2 = Personagens('Tiana', 'A princesa e o sapo', 'Protagonista')
    print(" ༘ Diretorº 1:  ༘")
    print("  Nome:", d1.get_nome())
    print("  CPF:", d1.get_cpf())
    print("  Salário:", d1.get_tema())
    print(" ༘ Diretorº 2:  ༘")
    print("  Nome:", d2.get_nome())
    print("  CPF:", d2.get_cpf())
    print("  Salário:", tb2.get_tema())
    print(" ༘ Personagemº 1:  ༘")
    print("  Nome:", p1.get_nome())
    print("  Desenho:", p1.get_desenho())
    print("  Cargo:", p1.get_cargo())
    print(" ༘ Personagemº 2:  ༘")
    print("  Nome:", p1.get_nome())
    print("  Desenho:", p1.get_desenho())
    print("  Cargo:", p1.get_cargo())

# 8. E teste (use) todos os métodos desenvolvidos nas classes.

class Disney():
    def __init__(self, nome, cpf, salario=float, cargo='animador'):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.cargo = cargo
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_cpf(self):
        return self.cpf
    def set_cpf(self, novo_cpf):
        self.cpf = novo_cpf
    def get_salario(self):
        return self.salario
    def set_salario(self, novo_salario):
        if self.salario <= 0.0:
            print('Novo salário inválido!')
        self.salario = novo_salario
    def get_cargo(self):
        return self.cargo
    def set_cargo(self, novo_cargo):
        self.cargo = novo_cargo
    def retorna_dados(self):
        dados = f"Nome: {self.get_nome()}\nCPF: {self.get_cpf()}\nSalário: {self.get_salario()}\nCargo: {self.get_cargo()}"
        return dados

class Diretor(Disney):
    def __init__(self, nome, cpf, tema):
        self.tema = tema
        super().__init__(nome, cpf)
    def get_tema(self):
        return self.tema
    def set_tema(self, novo_tema):
        self.tema = novo_tema
class Personagens(Disney):
    def __init__(self, nome, desenho, cargo):
        self.desenho = desenho
        super().__init__(nome, cargo)
    def get_desenho(self):
        return self.desenho
    def set_desenho(self, novo_desenho):
        self.desenho = novo_desenho

if __name__ == '__main__':
    tb1 = Disney('Rogério', '178.897.456-91', 17.000, 'Engenheiro')
    tb2 = Disney('Marcos', '785.443.289-26', 25.000)
    print(" ༘ Trabalhadorº 1:  ༘")
    print("  Nome:", tb1.get_nome())
    print("  CPF:", tb1.get_cpf())
    print("  Salário:", tb1.get_salario())
    print("  Cargo:", tb1.get_cargo())
    print('Dados concatenados do Trabalhador nº 1:\n', tb1.retorna_dados())
    print("--------------------")
    print(" ༘ Trabalhadorº 2:  ༘")
    print("  Nome:", tb2.get_nome())
    print("  CPF:", tb2.get_cpf())
    print("  Salário:", tb2.get_salario())
    print("  Cargo:", tb2.get_cargo())
    nvs = input('Digite o valor do novo salário: ')
    tb2.set_salario(nvs)
    print("Salário atualizado: ", tb2.get_salario())
    d1 = Diretor('Fábio', '785.449.234-89', 'Filmagem')
    d2 = Diretor('Leogis', '665.429.564-90', 'Luzes')
    p1 = Personagens('Mickey', 'A casa do Mickey Mouse', 'Protagonista')
    p2 = Personagens('Tiana', 'A princesa e o sapo', 'Protagonista')
    print(" ༘ Diretorº 1:  ༘")
    print("  Nome:", d1.get_nome())
    print("  CPF:", d1.get_cpf())
    print("  Salário:", d1.get_tema())
    print(" ༘ Diretorº 2:  ༘")
    print("  Nome:", d2.get_nome())
    print("  CPF:", d2.get_cpf())
    print("  Salário:", tb2.get_tema())
    print(" ༘ Personagemº 1:  ༘")
    print("  Nome:", p1.get_nome())
    print("  Desenho:", p1.get_desenho())
    print("  Cargo:", p1.get_cargo())
    print(" ༘ Personagemº 2:  ༘")
    print("  Nome:", p1.get_nome())
    print("  Desenho:", p1.get_desenho())
    print("  Cargo:", p1.get_cargo())
    nnv = input("Digite o novo nome para Mickey: ")
    p1.set_nome(nnv)
    print("Nome do Personagem atualizado: ", p1.get_nome())
    ntd = input("Digite o novo tema de direção: ")
    d1.set_tema(ntd)
    print("Novo tema do diretor: ", d1.get_tema())

# Código de Luísa Amâncio Brambilla - Turma B - Matutino.