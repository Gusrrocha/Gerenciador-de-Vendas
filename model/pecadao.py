lista_pecas = []
def getPeca(id):
    for p in lista_pecas:
        if p.id == id:
            return p

def add(nova_peca):
    novo_id = len(lista_pecas)+1
    nova_peca.id = novo_id
    lista_pecas.append(nova_peca)

def edit(peca):
    for index in range(0, len(lista_pecas)):
        peca_atual = lista_pecas[index]
        if peca.id == peca_atual.id:
            del lista_pecas[index]

            return

def delete():
    pass

def lista_peca():
    pass
