import sys
import qttest



app = qttest.Ui_MainWindow(sys.argv)
mainWindow = QMainWindow()
ui = Ui_mainWindow()
ui.setupUi(mainWindow)
mainWindow.show()
sys.exit(app.exec_())
exit(app.exec_())
