# -*- coding: utf-8 -*-
import sys,subprocess
import os
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui, Qt

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(490, 190)
        MainWindow.setMinimumSize(QtCore.QSize(490, 190))
        MainWindow.setMaximumSize(QtCore.QSize(490, 190))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/4chan.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 238);\n"
"font: 75 8pt \"Meiryo\";\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(9, 0, 78, 75))
        self.frame.setStyleSheet(_fromUtf8("background-image: url(:/img/img/4chan.png);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(100, 5, 386, 156))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayoutWidget = QtGui.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(8, 15, 372, 134))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        spacerItem = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout.setItem(0, QtGui.QFormLayout.LabelRole, spacerItem)
        self.linkToBoardWithImagesLabel = QtGui.QLabel(self.formLayoutWidget)
        self.linkToBoardWithImagesLabel.setObjectName(_fromUtf8("linkToBoardWithImagesLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.linkToBoardWithImagesLabel)
        self.linkToBoardLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.linkToBoardLineEdit.setEnabled(True)
        self.linkToBoardLineEdit.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.511364, y2:1, stop:0 rgba(255, 255, 210, 255), stop:1 rgba(255, 255, 180, 255));"))
        self.linkToBoardLineEdit.setObjectName(_fromUtf8("linkToBoardLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.linkToBoardLineEdit)
        self.outputDirectoryLabel = QtGui.QLabel(self.formLayoutWidget)
        self.outputDirectoryLabel.setObjectName(_fromUtf8("outputDirectoryLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.outputDirectoryLabel)
        self.getDirectoryButton = QtGui.QPushButton(self.formLayoutWidget)
        self.getDirectoryButton.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.511364, y2:1, stop:0 rgba(255, 255, 210, 255), stop:1 rgba(255, 255, 180, 255));"))
        self.getDirectoryButton.setObjectName(_fromUtf8("getDirectoryButton"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.getDirectoryButton)
        self.goButton = QtGui.QPushButton(self.formLayoutWidget)
        self.goButton.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.511364, y2:1, stop:0 rgba(255, 255, 210, 255), stop:1 rgba(255, 255, 180, 255));"))
        self.goButton.setObjectName(_fromUtf8("goButton"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.goButton)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtGui.QFormLayout.FieldRole, spacerItem1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(2, QtGui.QFormLayout.FieldRole, spacerItem2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "4 Chan Image Scraper", None))
        self.groupBox.setTitle(_translate("MainWindow", "4 Chan Image Scraper", None))
        self.linkToBoardWithImagesLabel.setText(_translate("MainWindow", "Link to Board with Images:", None))
        self.outputDirectoryLabel.setText(_translate("MainWindow", "Output Directory:", None))
        self.getDirectoryButton.setText(_translate("MainWindow", "Choose Path", None))
        self.goButton.setText(_translate("MainWindow", "Go", None))

    import resources

if __name__ == "__main__":

   
    app = QApplication(sys.argv)
    
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())

