# Descrição: Classe Cliente
# Contém os atributos do cliente

class Cliente():
    def __init__(self, id, nome, endereco, telefone):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    def imprime(self):
        print(f"ID - {self.id}, NOME - {self.nome}, ENDEREÇO - {self.endereco}, TELEFONE - {self.telefone}")
        