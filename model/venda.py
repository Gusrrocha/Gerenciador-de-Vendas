# Descrição: Venda

from model.cliente import Cliente


class Venda():
    def __init__(self, id, cliente, data, lista_de_itens):
        self.id = id
        self.cliente = cliente
        self.data = data
        self.lista_de_itens = lista_de_itens

    def valorTotal(self):
        vtotal = 0
        for peca in self.lista_de_itens:
            vtotal += peca.valor
        return vtotal