import sys, random
from salaryUi import Ui_MainWindow
from PyQt5 import QtWidgets
#

class salaryWindow(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setMouseTracking(True)
        self.ui.centralwidget.setMouseTracking(True)
        self.ui.centralwidget.installEventFilter(self)
        self.ui.noButton.setMouseTracking(True)
        
        self.centerTrigger = 0

        self.ui.dialog = QtWidgets.QMessageBox(self.ui.centralwidget)
        self.ui.dialog.setWindowTitle("Hooray!")
        self.ui.dialog.setText("Glad to hear that you're so satisfied with your salary!")
        
        self.addAllConnections()
        
        
    def mouseMoveEvent(self, event):
        pos = event.pos()
        
        x = self.ui.noButton.geometry().x( )
        y = self.ui.noButton.geometry().y( )
        w = self.ui.noButton.geometry().width( )
        h = self.ui.noButton.geometry().height( )
        
        dist = self.distance(pos.x(), pos.y(), x, y, w, h)
        
        if dist == 0:
            if self.centerTrigger == 0:
                self.ui.noButton.setText("Yes")
                self.ui.yesButton.setText("No")
                self.centerTrigger = 1
            
        elif dist < 500:
            x, y = self.generateNewPosition()
            self.ui.noButton.setGeometry(x, y, w, h)
            
            if self.centerTrigger == 1:
                self.centerTrigger = 0
                self.ui.noButton.setText('No')
                self.ui.yesButton.setText('Yes')
                
        else:
            if self.centerTrigger == 1:
                self.centerTrigger = 0
                self.ui.noButton.setText('No')
                self.ui.yesButton.setText('Yes')
                
    def addAllConnections(self):
        
        self.ui.yesButton.clicked.connect(self.yesConnect)
        self.ui.noButton.pressed.connect(self.noConnect)
        self.ui.noButton.released.connect(self.noRLSDConnect)
        self.ui.dialog.buttonClicked.connect(self.btnClickedConnect)


    def btnClickedConnect(self):
        
        sys.exit()
    
    
    def yesConnect(self):
        
        self.ui.dialog.open()
        
        
    def noConnect(self):
        
        self.ui.yesButton.setText('No')
        self.ui.noButton.setText('Yes')
        
        self.setMouseTracking(False)
        
        
    def noRLSDConnect(self):
        
        self.ui.dialog.open()


    def generateNewPosition(self):
        
        w = self.ui.noButton.geometry().width()
        h = self.ui.noButton.geometry().height()
        
        newx = random.randint(1, self.geometry().width() - w)
        newy = random.randint(1, self.geometry().height() - h)
        
        x = self.ui.yesButton.geometry().x()
        y = self.ui.yesButton.geometry().y()
        
        if self.distance(newx, newy, x, y, w, h) < 700 or \
           self.distance(newx+w, newy, x, y, w, h) < 700 or \
           self.distance(newx, newy + h, x, y, w, h) < 700 or \
           self.distance(newx+w, newy+h, x, y, w, h) < 700:
#            print('fuck', x,y,newx,newy, self.distance(newx,newy,x,y,w,h) )
            return self.generateNewPosition()
#
#        print('why', x,y,newx,newy, self.distance(newx,newy,x,y,w,h), 
#              self.distance(newx+w, newy, x, y, w, h) , 
#              self.distance(newx, newy + h, x, y, w, h), 
#              self.distance(newx+w, newy+h, x, y, w, h) )
        
        return newx, newy
        


    def distance(self, x1, y1, x2, y2, w, h):
        
        #print(x1, y1, x2, y2, w, h)
        
        
        if x1 < x2 and y1 < y2:
#            print(1)
            return (y2 - y1)**2 + (x2 - x1)**2
        
        elif x1 < x2 and y1 > y2 + h:
#            print(2)
            return (y2 + h - y1)**2 + (x2 - x1)**2
        
        elif x1 < x2 and y1 > y2:
#            print(3)
            return (x2 - x1)**2
            
        elif x1 > x2 + w and y1 < y2:
#            print(4)
            return (y2 - y1)**2 + (x2 + w - x1)**2
            
        elif x1 > x2 and y1 < y2 and x1 < x2 + w:
#            print(5)
            return (y2 - y1)**2
        
        elif x1 > x2 and x1 < x2 + w and y1 > y2 + h:
#            print(6)
            return (y2 - y1 + h)**2
            
        elif x1 > x2 + w and y1 > y2 and y1 < y2 + h:
#            print(7)
            return (x2 + w - x1)**2
        
        elif x1 > x2 + w and y1 > y2 + h:
#            print(8)
            return (x2 + w - x1)**2 + (y2 + h - y1)**2
        
        
        else:
            return 0
        

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    win = salaryWindow()
    win.show()
    sys.exit(app.exec_())
