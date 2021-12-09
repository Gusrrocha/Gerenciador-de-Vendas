# Classe que irá controlar o main_window.ui

from qt_core import *
from controller.cliente_page import ClientesPage
from controller.pecas_page import PecasPage
from controller.resumo_page import ResumoPage
from controller.vendas_page import VendasPage
FILE_UI = 'view/mainwindow.ui'
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        # criar os objetos referentes as páginas
        self.resumo_page = ResumoPage()
        self.clientes_page = ClientesPage()
        self.pecas_page = PecasPage()
        self.vendas_page = VendasPage()

        # Adicionar as páginas ao painel_principal
        self.painel_principal.insertWidget(0,self.resumo_page)
        self.painel_principal.insertWidget(1,self.clientes_page)
        self.painel_principal.insertWidget(2,self.pecas_page)
        self.painel_principal.insertWidget(3,self.vendas_page)
        # define o evento/ação dos botão:
        self.resumo_btn.clicked.connect(self.show_resumo)
        self.clientes_btn.clicked.connect(self.show_clientes)
        self.pecas_btn.clicked.connect(self.show_pecas)
        self.vendas_btn.clicked.connect(self.show_vendas)
    def show_resumo(self):
        self.painel_principal.setCurrentIndex(0)
    
    def show_clientes(self):
        self.painel_principal.setCurrentIndex(1)

    def show_pecas(self):
        self.painel_principal.setCurrentIndex(2)

    def show_vendas(self):
        self.painel_principal.setCurrentIndex(3)