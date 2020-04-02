###########################################################################
#                                                                         #
#   Brief:           COM communication                                    #
#   Modified by:     Jeferson Pazze  (jeferson.pazze@tothlifecare.com)    #
#   Date:            03/20/2020                                           #
#   Modify:          04/02/2020                                           #
#                                                                         #
###########################################################################

import serial
import matplotlib.pyplot as plt
from config_AD71244 import *
import atexit
import time
import matplotlib.animation as animation
import datetime as dt
from random import randint
import numpy as np
import math
import openpyxl, os
import xlwt
from datetime import datetime


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

xs = []
ys = []
ws = []
zs = []

voltage = []
AD = []

serialArduino = serial.Serial(DEVICE , BAUD_RATE, timeout= TIMEOUT )
time.sleep(1)

def moving_average(x, w):
    conv = np.convolve(x, np.ones(w), 'valid')
    teste = np.mean(conv)
    return teste

def animate(i, xs, ys, ws):

    plt.ion()

    var1 = "S"
    serialArduino.write(str.encode(var1))                    
    serialArduino.write(str.encode(var1)) 

    data = serialArduino.readline().decode('ascii') 
    lines = data.split(' ')
    a, b, c, d, e = lines
    
    vetor = np.asarray(lines)
    voltage = float((vetor[3]))
    AD = int((vetor[1]))

    calc = ((AD*2.5)/ ((2 ** 24)-1))

    teste = float(moving_average(voltage, 10))

    xs.append(dt.datetime.now().strftime('%S.%f'))
    ys.append(calc)
    ws.append(teste)

    xs = xs[-25:]
    ys = ys[-25:]
    ws = ws[-25:]


    ax.clear()
    ax.plot(xs, ys, ws)

    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Catheter Calibration System (Real-Time)')
    plt.ylabel('Voltage (V)')
    plt.xlabel('Time (s)')
    ax.legend(['Valor Calculado', 'Média'])
    plt.grid()

while 1:
    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys, ws), interval=1)
    plt.show()
    
# Set up plot to call animate() function periodically

