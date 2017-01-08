import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic, QtCore, QtGui
import pupil

Ui_MainWindow, QtBaseClass = uic.loadUiType("SafetyFirst.ui")

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.StartMonitoring)
        #self.ui.closeButton.clicked.connect(self, Qt.SIGNAL('triggered()'), self.closeEvent)

    def StartMonitoring(self):
        #price = int(self.ui.price_box.toPlainText())
        #tax = (self.ui.tax_rate.value())
        #total_price = price + ((tax / 100) * price)
        #total_price_string = “The total price with tax is: ” + str(total_price)
        #self.ui.results_window.setText(total_price_string)
        self.ui.pushButton.setText("Monitoring!")
        self.ui.pushButton.setStyleSheet("background-image: url(red.png);")
        QApplication.processEvents()
        pupil.main()
    
    def closeEvent(self, event):
        print("Closing")
        self.destory()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    #window.show()
    window.showMaximized()
    sys.exit(app.exec_())