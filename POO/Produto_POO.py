class Produto:
    def __init__(self, nome, vlr_compra, vlr_venda, qtd_estoque, qtd_minima):
        self.nome = nome
        self.vlr_compra = vlr_compra
        self.vlr_venda = vlr_venda
        self.qtd_estoque = qtd_estoque
        self.qtd_minima = qtd_minima
    def get_nome(self):
        return self.nome
    def set_nome(self, nome):
        if isinstance(nome, str):
            self.nome = nome
        else:
            print("O nome precisa ser uma string.")
    def get_qtd_estoque(self):
        return self.qtd_estoque
    def set_qtd_estoque(self, qtd_estoque):
        if isinstance(qtd_estoque, int):
            self.qtd_estoque = qtd_estoque
        else:
            print("A quantidade em estoque precisa ser um número inteiro.")
    def get_qtd_minima(self):
        return self.qtd_minima
    def set_qtd_minima(self, qtd_minima):
        if isinstance(qtd_minima, int):
            self.qtd_minima = qtd_minima
        else:
            print("A quantidade mínima precisa ser um número inteiro.")
    def set_vlr_compra(self, vlr_compra):
        if isinstance(vlr_compra, (int, float)) and vlr_compra > 0:
            self.vlr_compra = vlr_compra
        else:
            print("O valor de compra precisa ser um número positivo.")
    def __str__(self):
        return f"Produto: {self.nome} | Valor de compra: {self.vlr_compra} | Valor de venda: {self.vlr_venda} | Quantidade em estoque: {self.qtd_estoque} | Quantidade mínima: {self.qtd_minima}"
    def lucro(self):
        return self.qtd_estoque * (self.vlr_venda - self.vlr_compra)
    def atualiza_estoque(self, qtd_vendida):
        if self.qtd_estoque - qtd_vendida >= 0:
            self.qtd_estoque -= qtd_vendida
        else:
            print("A quantidade vendida é maior do que a quantidade em estoque.")
    def alerta_estoque(self):
        if self.qtd_estoque < self.qtd_minima:
            return True
        else:
            return False
    def repor_produto(self, qtd_adquirida):
        self.qtd_estoque += qtd_adquirida
    def maior_qtd(produto1, produto2):
        if produto1.qtd_estoque > produto2.qtd_estoque:
            return produto1
        else:
            return produto2
    def maior_lucro(produto1, produto2):
        if produto1.lucro() > produto2.lucro():
            return produto1
        else:
            return produto2

if __name__ == '__main__':
    p1 = Produto("Arroz", 15.00, 19.50, 67, 20)
    print(p1)
    p1.set_qtd_minima(15)
    p2 = Produto("Feijão")
    p3 = Produto("Óleo de Soja", 5.00)
    p1.atualiza_estoque()
