from qt_core import *
FILE_UI = 'view/vendas_page.ui'

class VendasPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)