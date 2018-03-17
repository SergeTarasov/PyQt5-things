#!/usr/bin/python3
# -*- coding: utf-8 -*-

import  sys
try:
	from PyQt5 import QtCore, QtGui, QtWidgets
except:
	print('Package pyqt5 is not installed. Try: pip3 install pyqt5')
	
from mines import Ui_MainWindow
from minesweeper import Minesweeper

    
class MinesweeperWindow(Ui_MainWindow):
    
    def __init__(self, MainWindow):
        Ui_MainWindow.__init__(self)

        self.game = Minesweeper()
        self.timer = QtCore.QTimer(MainWindow)
        self.mouseTimer = QtCore.QTimer(MainWindow)
        
        self.mineFlagIcon = QtGui.QPixmap('flag.png')
        
        self.smileIcon = QtGui.QIcon(QtGui.QPixmap('smile.png'))
        self.winIcon = QtGui.QIcon(QtGui.QPixmap('win.png'))
        self.mineIcon = QtGui.QIcon(QtGui.QPixmap('mine.png'))
        self.openIcon = QtGui.QIcon(QtGui.QPixmap('open.png'))
        
        self.smiles = {'smile': self.smileIcon, 'open':self.openIcon, 'mine':self.mineIcon, 'win':self.winIcon}
        self.currentSmile = 'smile'
        
        self.level = 0.13
        self.size = (0,0)
        
        self.minesText = str(int(self.level*100))+"%"
        self.timeText = '-- : --'

        self.setupUi(MainWindow)
        self.addAllConnections()
        self.updateWindow()

	
    def addAllConnections(self):
        
    #start screen
        self.pushButton_9x9.clicked.connect(self.pB9x9Connect)
        self.pushButton_16x16.clicked.connect(self.pB16x16Connect)
        self.pushButton_16x30.clicked.connect(self.pB16x30Connect)
        self.levelBox.currentIndexChanged.connect(self.levelConnect)
    
    #restart button (smile)
        self.smileButton.clicked.connect(self.restartGame)
        
    #timer
        self.timer.timeout.connect(self.updateTimer)
        
    #Game menu
        self.actionNew_game.triggered.connect(self.newGameAction)
        self.actionRestart.triggered.connect(self.restartGame)
        self.actionExit.triggered.connect(self.exitAction)
        
	
    def updateWindow(self):
        
        self.labelMines.setText(str(self.minesText))
        self.labelTime.setText(str(self.timeText))

        self.smileButton.setIcon(self.smiles[self.currentSmile])
        self.smileButton.setIconSize(QtCore.QSize(29,29))

        
    def newGameAction(self):
        
        #stop the game
        self.timer.stop()
        self.timeText = '-- : --'
        self.minesText = str(int(100* self.level))+'%'
        #0 - new game screen, 1 - field screen
        self.stackedWidget.setCurrentIndex(0)
        self.closeField()
        self.updateWindow()
                

    def restartGameAction(self):
        self.timer.stop()
        self.closeField()
        self.updateWindow()
        self.initGame()
        
	
    def exitAction(self):
        sys.exit()
        
    def pB9x9Connect(self):
        self.size = (9,9)
        self.initGame()
        
    def pB16x16Connect(self):
        self.size = (16,16)
        self.initGame()
        
    def pB16x30Connect(self):
        self.size = (16,30)
        self.initGame()
        
	
    def levelConnect(self):
        
        index = self.levelBox.currentText()
        if index == "easy":
            self.level = 0.13
        elif index == "normal":
            self.level = 0.18
        elif index == "hard":
            self.level = 0.23
        elif index == "insane":
            self.level = 0.27
        
        self.updateWindow()
    
    
    def initGame(self):
        
        self.time = 0
        self.minesText = str(int(self.size[0]*self.size[1]* self.level))
        self.currentSmile = 'smile'
        
        self.game.startGame( self.size, int(self.size[0]*self.size[1]* self.level) )
        self.stackedWidget.setCurrentIndex(1)
        self.updateWindow()
        self.initField()
        
        
    def gameOver(self):
        self.timer.stop()
        self.openField(openAll = 1)
        self.currentSmile = 'mine'
        self.updateWindow()
        
	
    def restartGame(self):
        
        self.timer.stop()
        self.time = 0
        self.timeText = '00 : 00'
        self.updateWindow()
        self.closeField()
        self.initGame()
        
        
    def winner(self):
        
        self.timer.stop()
        self.setFlag(0, markLeft = 1)
        self.minesText = "Win!"
        self.labelMines.setText(self.minesText)
        
    
    def initField(self):
        
        positions = [(i,j) for i in range(self.size[0]) for j in range(self.size[1])]
    
        for position in positions:
            self.gameGrid.addWidget(self.createRlckButton(), *position)
	
        MainWindow.resize(*self.size)
        MainWindow.setMaximumSize(QtCore.QSize(self.size[1] * 20 +  13, self.size[0] * 20 + 82))
        
	
    def openField(self, oplist = [], openAll = 0):
        
        if openAll == 1:
            oplist = self.game.restL.copy()
        
	
        for i in oplist:
            
            fValue = self.game.rHint(i)
        
            if i  in self.game.flags:
                if openAll == 0:
                    continue
                
                elif fValue != -1:
                    self.setFlag(i) #unflag and
                    self.gameGrid.itemAt(i).widget().setText("X")   #draw cross on the button
                    continue 
                
                elif fValue == -1:
                    continue 
            
            if fValue == -1:
                fValue = '*'
		
            elif fValue == 0:
                fValue = ' '
            
            lbl = QtWidgets.QLabel(str(fValue))
            label = dclkLabel(lbl)
            label.setAlignment( QtCore.Qt.AlignCenter )
            label.setFixedSize(QtCore.QSize(20, 20))
            label.bthClick.connect(self.openNeighbors)
            label.setText(str(fValue))
            
            #if fValue == '*':
            #    label.setStyleSheet("QLabel{border:0.5px solid rgb(120,40,40);}")
            if fValue == 1:
                label.setStyleSheet("QLabel{ color: blue}")
            elif fValue == 2:
                label.setStyleSheet("QLabel{ color: green }")
            elif fValue == 3:
                label.setStyleSheet("QLabel{ color: red }")
            elif fValue == 4:
                label.setStyleSheet("QLabel{ color: rgb(51,51,153) }")
            elif fValue == 5:
                label.setStyleSheet("QLabel{ color: rgb(153, 0, 0) }")
            elif fValue == 6:
                label.setStyleSheet("QLabel{ color: yellow }")
            elif fValue == 7:
                label.setStyleSheet("QLabel{ color: rgb(204, 0, 102) }")
            elif fValue == 8:
                label.setStyleSheet("QLabel{ color: rgb(255, 0, 102) }")
                    
               
            button = self.gameGrid.itemAt(i).widget()
            self.gameGrid.replaceWidget(button, label)
            button.hide()

            self.game.openCell(i)

            if self.game.flagsLeft == self.game.cellsLeft and openAll == 0:
                self.winner()
        
        
    def closeField(self):
        
        if self.gameGrid.itemAt(0) != None:
            for i in range(self.game.total):
                
                element = self.gameGrid.itemAt(0).widget()
                self.gameGrid.removeWidget(element)
                element.hide()
    
    def fieldClicked(self):
        
        if self.timer.isActive() == 0 and self.time == 0:
            self.timer.start(1000)
            self.updateTimer()
            self.gameTrigger = 1
            
        elif self.timer.isActive() == False:
            return
        
        button = MainWindow.sender()
        idx = self.gameGrid.indexOf(button)
        
        if idx in self.game.flags:
            return
        
        fValue = self.game.rHint(idx)
        
        if fValue == -1:
            self.gameOver()
        
        elif fValue == 0:
            self.zeroClicked(idx)
            
        else:
            self.openField([idx])
    
    def mineFlagged(self):  
        
        if self.timer.isActive() != True:
            return
        button = MainWindow.sender()
        idx = self.gameGrid.indexOf(button)
        self.setFlag(idx)
    
    
    def setFlag(self, idx, markLeft = 0):
        
        button = self.gameGrid.itemAt(idx).widget()

        if markLeft == 1:
            
            for i in self.game.restL:
                
                button = self.gameGrid.itemAt(i).widget()
                if i not in self.game.flags:
                    self.game.flagCell(i)
                            
                    button.setIcon(QtGui.QIcon(self.mineFlagIcon))
                    button.setIconSize(QtCore.QSize(20,20))            
                    
        elif self.game.flagCell(idx) == 1:
            button.setIcon(QtGui.QIcon(self.mineFlagIcon))
            button.setIconSize(QtCore.QSize(20,20))

        else:
            button.setIconSize(QtCore.QSize(0,0))
        
        self.updateMines()
        
    def updateMines(self):
        self.minesText = str(self.game.flagsLeft)
        self.labelMines.setText(self.minesText)

        
    def updateTimer(self):
        self.updateTimeLabel()
        self.time += 1
        
    def updateTimeLabel(self):
        
        minutes = int(self.time / 60)
        seconds =     self.time % 60
        self.timeText = (str(minutes) if minutes >= 10 else ( '0' + str(minutes) ) ) + \
                ' : ' + (str(seconds) if seconds >= 10 else ( '0' + str(seconds) ) )
        
        self.labelTime.setText(self.timeText)


    def zeroClicked(self, idx):
        
        pp = self.game.openMeadow( idx )
        self.openField( oplist = pp )
        
    
    def createRlckButton(self):
        
        button = rclkPButton(self.fieldWidget)

        button.setFixedSize(QtCore.QSize(20, 20))
        button.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        
        button.clicked.connect(self.fieldClicked)
        button.rightClick.connect(self.mineFlagged)
        button.pressed.connect(self.onclick)
        button.released.connect(self.onrelease)
        button.bothClick.connect(self.openNeighbors)
        
        return button

    def openNeighbors(self):
        button = MainWindow.sender()
        idx = self.gameGrid.indexOf(button)
        opl = []
        for i in self.game.neighbors(idx):
            
            if i not in self.game.flags and i not in self.game.openL:
                if i not in opl:
                    opl.append(i)
                hint = self.game.rHint(i)
                if hint == -1:
                    self.gameOver()
                    return
                
                elif hint == 0:
                    for j in self.game.openMeadow(idx):
                        if j not in opl:
                            opl.append(j)
                
        self.openField(oplist = opl)
    
    def onclick(self):
        
        if self.timer.isActive() != True:
            return
        
        self.smileButton.setIcon(self.openIcon)
        self.smileButton.setIconSize(QtCore.QSize(29,29))
    
    
    def onrelease(self):
        
        if self.timer.isActive() != True:
            return
        
        self.smileButton.setIcon(self.smileIcon)
        self.smileButton.setIconSize(QtCore.QSize(29,29))
    
class rclkPButton(QtWidgets.QPushButton):
    
    rightClick = QtCore.pyqtSignal()
    bothClick = QtCore.pyqtSignal()
    
    def __init__(self, parent):
        QtWidgets.QPushButton.__init__(self, parent)
        
    def mousePressEvent(self, event):
        QtWidgets.QPushButton.mousePressEvent(self, event)
        
        #4 is the number of the central(wheel) button
        if event.button() == 4:
            self.bothClick.emit()
        
        elif event.button() == QtCore.Qt.RightButton:
            self.rightClick.emit()
          
class dclkLabel(QtWidgets.QLabel):
    bthClick = QtCore.pyqtSignal()

    def __init__(self, parent):
        QtWidgets.QLabel.__init__(self, parent)
    
    def mousePressEvent(self, event):
        
        QtWidgets.QLabel.mousePressEvent(self, event)

        #4 is the number of the central(wheel) button
        if event.button() == 4:
            self.bthClick.emit()
            
if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    
    ex = MinesweeperWindow(MainWindow)
    
    MainWindow.show()
    sys.exit(app.exec_())
