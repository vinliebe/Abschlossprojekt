import gui
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow


class MainForm(QMainWindow):
    def __init__(self,parent=None):
        super(MainForm,self).__init__(parent)
        self.ui = gui.Ui_Form()
        self.ui.setupUi(self)
    
if __name__ == "__main__":

    app = QApplication(sys.argv)

    form = MainForm()

    form.show()
    
    exit(app.exec_())
