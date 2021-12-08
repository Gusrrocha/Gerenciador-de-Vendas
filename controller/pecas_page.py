from controller.cad_peca import CadPecaWindow
from qt_core import *
import model.pecadao as funcoes_pecas

FILE_UI = 'view/pecas_page.ui'

class PecasPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        self.peca_window = None

        self.carrega_dados()

        # evento do botão nova peça
        self.novo_btn.clicked.connect(self.nova_peca)

        # configurações da tabela
        self.tabela.verticalHeader().setVisible(False)
        self.tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabela.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tabela.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.tabela.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)

    def nova_peca(self):
        # criação da janela de cadastro
        self.peca_window = CadPecaWindow(self)
        self.peca_window.show()
        
    def carrega_dados(self):

        lista_pecas = funcoes_pecas.lista_pecas

        self.tabela.setRowCount(0)

        for peca in lista_pecas:
            self.add_linha(peca)

    def add_linha(self, peca):
        rowCount = self.tabela.rowCount()
        self.tabela.insertRow(rowCount)


        id = QTableWidgetItem(str(peca.id))
        nome = QTableWidgetItem(peca.nome)
        valor = QTableWidgetItem(peca.valor)
        validade = QTableWidgetItem(peca.validade)
        quantidade = QTableWidgetItem(peca.quantidade)


        self.tabela.setItem(rowCount, 0, id)
        self.tabela.setItem(rowCount, 1, nome)
        self.tabela.setItem(rowCount, 2, valor)
        self.tabela.setItem(rowCount, 3, validade)
        self.tabela.setItem(rowCount, 4, quantidade)
        