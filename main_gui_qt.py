import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic, QtCore, QtGui
import pupil
import tty
import termios

Ui_MainWindow, QtBaseClass = uic.loadUiType("SafetyFirst.ui")
class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.state = 'Start'
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.ButtonBehaviour)
        self.ui.quit.clicked.connect(self.quit)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.state = 'Stop'
            self.StopMonitoring()
          #self.ui.pushButton.clicked.connect(self.StartMonitoring)

    def ButtonBehaviour(self):
        if self.state is 'Start':
            self.state='Monitoring'
            self.StartMonitoring()

    def StartMonitoring(self):
        print(self.state)
        self.ui.pushButton.setText("Monitoring!")
        self.ui.pushButton.setStyleSheet("background-image: url(red.png);")
        QApplication.processEvents()
        pupil.main()
        if self.state == 'Start':
            self.state = 'Stop'
            self.StopMonitoring()

    def StopMonitoring(self):
        print(self.state)
        self.state='Start'
        self.ui.pushButton.setText("Start Monitoring!")
        self.ui.pushButton.setStyleSheet("background-image: url(green.png);")
   
    def quit(self):
        sys.exit(0)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    #window.show()
    window.showMaximized()
    sys.exit(app.exec_())