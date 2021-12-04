from qt_core import *
FILE_UI = 'view/pecas_page.ui'
class PecasPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)