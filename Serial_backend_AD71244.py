###########################################################################
#                                                                         #
#   Brief:           COM communication                                    #
#   Modified by:     Jeferson Pazze  (jeferson.pazze@tothlifecare.com)    #
#   Date:            03/20/2020                                           #
#                                                                         #
###########################################################################

import serial
import time
from config_AD71244 import *
#from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5 import QtWidgets, uic
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from random import randint
import io


'''
app = QApplication([])
label = QLabel('Hello World!')
label.show()

app.exec_()
'''
'''
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()
app.exec_()

'''

# ser = serial.Serial(DEVICE , BAUD_RATE, timeout= TIMEOUT )
# # var = input("Enter something: ")
# # ser.write(str.encode(var))

# time.sleep(1)

# var1 = "S"                                      # Variavel que corresponde pela leitura de dados pelo AD
# ser.write(str.encode(var1))                     # Envia a solicitação para leitura de dados peço AD

# time.sleep(1)
# var2 = "C"                                      # Variavel que corresponde pela leitura de dados pelo AD de forma continua
# ser.write(str.encode(var2)) 
'''
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget),
        
        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]
        # hour = ser.readline()
        # temperature = ser.readline()

        self.graphWidget.setBackground('w')

        pen = pg.mkPen(color=(255, 0, 0))
        self.graphWidget.plot(hour, temperature, pen=pen)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    
    
'''
    

ser = serial.Serial(DEVICE , BAUD_RATE, timeout= TIMEOUT )
# var = input("Enter something: ")
# ser.write(str.encode(var))

##time.sleep(1)
##
##var1 = "S"                                      # Variavel que corresponde pela leitura de dados pelo AD
##ser.write(str.encode(var1))                     # Envia a solicitação para leitura de dados peço AD
##
##time.sleep(1)
##var2 = "C"                                      # Variavel que corresponde pela leitura de dados pelo AD de forma continua
##ser.write(str.encode(var2)) 

#ComSerial()
    
while 1:
    try:
        for i in range(0, 100):

            var1 = "S"                                      # Variavel que corresponde pela leitura de dados pelo AD
            ser.write(str.encode(var1))
            time.sleep(0.1)
            ser.write(str.encode(var1))
            time.sleep(0.1)
            
            data = ser.readline().decode('ascii')
            print("data: " , data)

            data1 = ser.readline()
            print("data1: " , data1)

            print('i: ', i)
            print('\n')
            print('-----------------------------------')
##            time.sleep(0.5)
            # var = input("Enter something: ")
            # ser.write(str.encode(var))
            
    except ser.SerialTimeoutException:
        print('Data could not be read')


