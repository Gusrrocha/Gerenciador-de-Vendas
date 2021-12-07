from qt_core import *
FILE_UI = 'view/cad_peca.ui'
class CadPecaWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)
