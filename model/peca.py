# Descrição: Peça
# Contém os atributos da peça

class Peça():
    def __init__(self, id, nome, valor, validade):
        self.id = id
        self.nome = nome
        self.valor = valor
        self.validade = validade

    def print(self):
        print(self.id, self.nome, self.valor, self.validade)