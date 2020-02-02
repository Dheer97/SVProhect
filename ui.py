
import sys
sys.path.append('C:/ProgramData/Anaconda3/Lib/site-packages')
from PyQt5 import QtCore, QtGui, QtWidgets

global test_path
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(700, 576)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.selectImageBtn = QtWidgets.QPushButton(self.centralwidget)
        self.selectImageBtn.setGeometry(QtCore.QRect(380, 380, 191, 31))
        self.selectImageBtn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.selectImageBtn.setObjectName("selectImageBtn")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 440, 161, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lblImage2 = QtWidgets.QLabel(self.centralwidget)
        self.lblImage2.setGeometry(QtCore.QRect(360, 160, 241, 191))
        self.lblImage2.setFrameShape(QtWidgets.QFrame.Box)
        self.lblImage2.setScaledContents(True)
        self.lblImage2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblImage2.setObjectName("lblImage2")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(0, 0, 701, 111))
        self.lblTitle.setMaximumSize(QtCore.QSize(701, 16777215))
        self.lblTitle.setFrameShadow(QtWidgets.QFrame.Plain)
        #self.lblTitle.setPixmap(QtGui.QPixmap("C:\\Users\\chava\\Desktop\\Signature-Verification-Form.jpg"))
        self.lblTitle.setScaledContents(True)
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.lblImage1 = QtWidgets.QLabel(self.centralwidget)
        self.lblImage1.setGeometry(QtCore.QRect(100, 160, 231, 191))
        self.lblImage1.setFrameShape(QtWidgets.QFrame.Box)
        self.lblImage1.setScaledContents(True)
        self.lblImage1.setObjectName("lblImage1")
        
        self.btnUpload1 = QtWidgets.QPushButton(self.centralwidget)
        self.btnUpload1.setGeometry(QtCore.QRect(140, 380, 171, 31))
        self.btnUpload1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btnUpload1.setObjectName("btnUpload1")
        self.output = QtWidgets.QLabel(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(254, 509, 191, 31))
        self.output.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.output.setObjectName("output")
        self.lblImage2.raise_()
        self.selectImageBtn.raise_()
        self.pushButton_2.raise_()
        self.lblTitle.raise_()
        self.lblImage1.raise_()
        self.btnUpload1.raise_()
        self.output.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #img1=self.btnUpload1.clicked.connect(self.setImage)
        #img2=self.selectImageBtn.clicked.connect(self.setImage2)
        #print("image1"+img1)
        #print(img1)
        #print("image2")
        #print(img2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.selectImageBtn.setText(_translate("MainWindow", "Upload Image"))
        self.pushButton_2.setText(_translate("MainWindow", "Verify"))
        self.btnUpload1.setText(_translate("MainWindow", "Upload Image"))

    def setImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Upload Image", "", "Image Files (*.png *.jpg *jpeg *.bmp)") # Ask for file
        print(fileName)
        if fileName: # If the user gives a file
            pixmap = QtGui.QPixmap(fileName) # Setup pixmap with the provided image
            
            pixmap = pixmap.scaled(self.lblImage1.width(), self.lblImage1.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
            self.lblImage1.setPixmap(pixmap) # Set the pixmap onto the label
            self.lblImage1.setAlignment(QtCore.Qt.AlignCenter) # Align the label to
        return fileName


    #Upload Image2
    def setImage2(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Upload Image", "", "Image Files (*.png *.jpg *jpeg *.bmp)") # Ask for file
        
        if fileName: # If the user gives a file
            pixmap = QtGui.QPixmap(fileName) # Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.lblImage2.width(), self.lblImage2.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
            self.lblImage2.setPixmap(pixmap) # Set the pixmap onto the label
            self.lblImage2.setAlignment(QtCore.Qt.AlignCenter) # Align the label to 
            
        return fileName





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    img1=ui.setImage()
    print("ui.setImage()")
    print(img1)

    #img1=ui.btnUpload1.clicked.connect(setImage())
    print(img1)
    #print(img1)


    MainWindow.show()
    
    #train_person_id = self.setImage()
    
    #print(train_person_id);

    sys.exit(app.exec_())
