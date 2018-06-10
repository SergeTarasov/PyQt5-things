import sys, os

import pyaudio  
import wave 
chunk = 1024

from pygame import mixer
from ipaUi import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

def play(filename):
    f = wave.open(filename, 'rb')
    p = pyaudio.PyAudio() 
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
            channels = f.getnchannels(),  
            rate = f.getframerate(),  
            output = True)  
    
    data = f.readframes(chunk)  
    while data:  
        stream.write(data)  
        data = f.readframes(chunk)  
       
    #stop stream  
    stream.stop_stream()  
    stream.close()  
    
    #close PyAudio  
    p.terminate() 
#        mixer.init()
#        mixer.music.load(self.location+'sounds/vowels/Close_back_rounded_vowel.mp3')
#        mixer.music.play()

class ipaWindow(Ui_MainWindow):
    
    def __init__(self, MainWindow):
        Ui_MainWindow.__init__(self)
        self.location = os.path.realpath(__file__)[:-len('ipa.py')]
        print(self.location)
        
        self.setupUi(MainWindow)
        
        self.addAllConnections()
    
    def addAllConnections(self):
        
        
        
        self.close_back_rounded_vowel.clicked.connect(self.close_back_rounded_vowelSound)
        self.close_back_unrounded_vowel.clicked.connect(self.close_back_unrounded_vowelSound)
        self.close_central_rounded_vowel.clicked.connect(self.close_central_rounded_vowelSound)
        self.close_central_unrounded_vowel.clicked.connect(self.close_central_unrounded_vowelSound)
        self.close_front_rounded_vowel.clicked.connect(self.close_front_rounded_vowelSound)
        self.close_front_unrounded_vowel.clicked.connect(self.close_front_unrounded_vowelSound)
        self.close_mid_back_rounded_vowel.clicked.connect(self.close_mid_back_rounded_vowelSound)
        self.close_mid_back_unrounded_vowel.clicked.connect(self.close_mid_back_unrounded_vowelSound)
        self.close_mid_central_rounded_vowel.clicked.connect(self.close_mid_central_rounded_vowelSound)
        self.close_mid_central_unrounded_vowel.clicked.connect(self.close_mid_central_unrounded_vowelSound)
        self.close_mid_front_unrounded_vowel.clicked.connect(self.close_mid_front_unrounded_vowelSound)
        self.close_mid_front_rounded_vowel.clicked.connect(self.close_mid_front_rounded_vowelSound)
        
        self.near_close_near_back_rounded_vowel.clicked.connect(self.near_close_near_back_rounded_vowelSound)
        self.near_close_near_front_rounded_vowel.clicked.connect(self.near_close_near_front_rounded_vowelSound)
        self.near_close_near_front_unrounded_vowel.clicked.connect(self.near_close_near_front_unrounded_vowelSound)
        self.near_open_central_unrounded_vowel.clicked.connect(self.near_open_central_unrounded_vowelSound)
        self.near_open_front_unrounded_vowel.clicked.connect(self.near_open_front_unrounded_vowelSound)
                
        self.mid_central_vowel.clicked.connect(self.mid_central_vowelSound)
                                               
        self.open_back_rounded_vowel.clicked.connect(self.open_back_rounded_vowelSound)
        self.open_back_unrounded_vowel.clicked.connect(self.open_back_unrounded_vowelSound)
        self.open_front_rounded_vowel.clicked.connect(self.open_front_rounded_vowelSound)
        self.open_front_unrounded_vowel.clicked.connect(self.open_front_unrounded_vowelSound)
        self.open_mid_back_rounded_vowel.clicked.connect(self.open_mid_back_rounded_vowelSound)
        self.open_mid_back_unrounded_vowel.clicked.connect(self.open_mid_back_unrounded_vowelSound)
        self.open_mid_central_rounded_vowel.clicked.connect(self.open_mid_central_rounded_vowelSound)
        self.open_mid_central_unrounded_vowel.clicked.connect(self.open_mid_central_unrounded_vowelSound)
        self.open_mid_front_rounded_vowel.clicked.connect(self.open_mid_front_rounded_vowelSound)
        self.open_mid_front_unrounded_vowel.clicked.connect(self.open_mid_front_unrounded_vowelSound)
        
        
    def close_back_rounded_vowelSound(self):
        play('sounds/vowels/Close_back_rounded_vowel.wav')
        
    def close_back_unrounded_vowelSound(self):
        play('sounds/vowels/Close_back_unrounded_vowel.wav')
        
    def close_central_rounded_vowelSound(self):
        play('sounds/vowels/Close_central_rounded_vowel.wav')
        
    def close_central_unrounded_vowelSound(self):
        play('sounds/vowels/Close_central_unrounded_vowel.wav')
        
    def close_front_rounded_vowelSound(self):
        play('sounds/vowels/Close_front_rounded_vowel.wav')
        
    def close_front_unrounded_vowelSound(self):
        play('sounds/vowels/Close_front_unrounded_vowel.wav')
        
    def close_mid_back_rounded_vowelSound(self):
        play('sounds/vowels/Close-mid_back_rounded_vowel.wav')
        
    def close_mid_back_unrounded_vowelSound(self):
        play('sounds/vowels/Close-mid_back_unrounded_vowel.wav')
        
    def close_mid_central_rounded_vowelSound(self):
        play('sounds/vowels/Close-mid_central_rounded_vowel.wav')
        
    def close_mid_central_unrounded_vowelSound(self):
        play('sounds/vowels/Close-mid_central_unrounded_vowel.wav')
        
    def close_mid_front_unrounded_vowelSound(self):
        play('sounds/vowels/Close-mid_front_unrounded_vowel.wav')
        
    def close_mid_front_rounded_vowelSound(self):
        play('sounds/vowels/Close-mid_front_rounded_vowel.wav')
        
        
        
        
    def near_close_near_back_rounded_vowelSound(self):
        play('sounds/vowels/Near-close_near-back_rounded_vowel.wav')
        
    def near_close_near_front_rounded_vowelSound(self):
        play('sounds/vowels/Near-close_near-front_rounded_vowel.wav')
        
    def near_close_near_front_unrounded_vowelSound(self):
        play('sounds/vowels/Near-close_near-front_unrounded_vowel.wav')
        
    def near_open_central_unrounded_vowelSound(self):
        play('sounds/vowels/Near-open_central_unrounded_vowel.wav')
        
    def near_open_front_unrounded_vowelSound(self):
        play('sounds/vowels/Near-open_front_unrounded_vowel.wav')
        
       
        
    def mid_central_vowelSound(self):
        play('sounds/vowels/Mid-central_vowel.wav')
        
        
        
    def open_back_rounded_vowelSound(self):
        play('sounds/vowels/Open_back_rounded_vowel.wav')
        
    def open_back_unrounded_vowelSound(self):
        play('sounds/vowels/Open_back_unrounded_vowel.wav')
        
    def open_front_rounded_vowelSound(self):
        play('sounds/vowels/Open_front_rounded_vowel.wav')
        
    def open_front_unrounded_vowelSound(self):
        play('sounds/vowels/Open_front_unrounded_vowel.wav')
        
    def open_mid_back_rounded_vowelSound(self):
        play('sounds/vowels/Open-mid_back_rounded_vowel.wav')
        
    def open_mid_back_unrounded_vowelSound(self):
        play('sounds/vowels/Open-mid_back_unrounded_vowel.wav')
        
    def open_mid_central_rounded_vowelSound(self):
        play('sounds/vowels/Open-mid_central_rounded_vowel.wav')
        
    def open_mid_central_unrounded_vowelSound(self):
        play('sounds/vowels/Open-mid_central_unrounded_vowel.wav')
        
    def open_mid_front_rounded_vowelSound(self):
        play('sounds/vowels/Open-mid_front_rounded_vowel.wav')
        
    def open_mid_front_unrounded_vowelSound(self):
        play('sounds/vowels/Open-mid_front_unrounded_vowel.wav')
        
        
        
        
        
if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow = QtWidgets.QMainWindow()
    
    ex = ipaWindow(MainWindow)
    
    MainWindow.show()
    sys.exit(app.exec_())
