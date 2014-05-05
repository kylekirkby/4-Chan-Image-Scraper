##Imports

import sys,subprocess
import os
from PyQt4.QtGui import QApplication, QDialog, QMainWindow,QTableWidget, QTableWidgetItem, QFileDialog
from PyQt4 import QtCore, QtGui, Qt
import urllib
from urllib.request import urlopen, URLopener
from bs4 import BeautifulSoup
import requests
from time import sleep
import resources

from mainWindow import Ui_MainWindow



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

class Main:
   def __init__(self):
      
      self.app = QApplication(sys.argv)
      self.window = QMainWindow()
      self.ui = Ui_MainWindow()
      self.ui.setupUi(self.window)
      self.window.show()
      self.ui.statusBar.showMessage("Ready...")
      #custom attribs

      self.directory = None

      #connections

      self.ui.getDirectoryButton.clicked.connect(self.getDirectory)
      self.ui.goButton.clicked.connect(self.getImages)
      
      sys.exit(self.app.exec_())
      
   def clear(self):
       
       self.ui.getDirectoryButton.setText(_translate("MainWindow","Choose Path", None))
       self.ui.linkToBoardLineEdit.clear()
       self.ui.statusBar.showMessage("Ready...")
      
      
   def getImages(self):
      
      if len(self.ui.linkToBoardLineEdit.text()) > 0:
         if self.directory != None:
            os.chdir(self.directory)
            url = self.ui.linkToBoardLineEdit.text()
            try:
                soup = urlopen(url).read()
                page = BeautifulSoup(soup)
                urls = []
                
                classes = page.findAll("a", { "class" : "fileThumb" })

                for each in classes:
                   img_link = each['href']
                   urls.append(img_link)

                   
                for num in range(0,len(urls)):
                   
                   filename = urls[num]
                   filename = filename.split('/')[-1]

                   outPath = self.directory + "/" + filename


                   newUrl = urls[num][2:]
         
                   
                   newUrl = "http://" + newUrl
                   response = requests.get(newUrl)
                   if response.status_code == 200:
                      message = str(num + 1) + " in " + str(len(urls)) + " | " + filename
                      self.ui.statusBar.showMessage(message)
                      with open(outPath, mode='wb') as out_file:
                         out_file.write(response.content)
                         out_file.close()
                os.startfile(self.directory)
                self.clear()

            except:
                self.ui.statusBar.showMessage("404 page not found...")
                sleep(1)
                self.clear()    
    
      #clear program
     
            
      

            
   def getDirectory(self):
      default_directory = os.path.expanduser('~') 
      directory = QFileDialog.getExistingDirectory(caption='Open', directory=default_directory)
      displayDirectory = directory[::-1]
      displayDirectory = displayDirectory[0:30]
      displayDirectory = displayDirectory[::-1]
      self.ui.getDirectoryButton.setText(_translate("MainWindow","..." + displayDirectory, None))
      
      self.directory = directory
if __name__ == "__main__":

   
    Main()
