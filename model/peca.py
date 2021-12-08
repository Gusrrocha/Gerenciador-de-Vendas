# Descrição: Peça
# Contém os atributos da peça

class Peca():
    def __init__(self, id, nome, valor, validade, quantidade):
        self.id = id
        self.nome = nome
        self.valor = valor
        self.validade = validade
        self.quantidade = quantidade

    def print(self):
        print(self.id, self.nome, self.valor, self.validade)