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

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

xs = []
ys = []

xs1 = []
ys1 = []

voltage = []
AD = []

serialArduino = serial.Serial(DEVICE , BAUD_RATE, timeout= TIMEOUT )
time.sleep(1)

def moving_average(voltage, n) :
    ret = np.cumsum(voltage, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    result = ret[n - 1:] / n
##    print('result: ', result)
    return result

def moving_average1(x, w):
    conv = np.convolve(x, np.ones(w), 'valid') / w
##    print('conv: ', conv)
    return conv

def animate(i, xs, ys):

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

    print('voltage: ',voltage)
    print('calc: ',calc)

    xs.append(dt.datetime.now().strftime('%S.%f'))#('%H:%M:%S'))
    ys.append(voltage)

    xs = xs[-25:]
    ys = ys[-25:]

    ax.clear()
    ax.plot(xs, ys)

    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Catheter Calibration System View')
    plt.ylabel('Voltage (V)')
    plt.xlabel('Time (s)')

    moving_average(voltage, 3)
    print(moving_average1(voltage, 3))

##    ax1 = plt.subplot(311)
##    plt.plot(calc, voltage)
##    plt.setp(ax1.get_xticklabels(), fontsize=6)
##
##    # share x only
##    ax2 = plt.subplot(312, sharex=ax1)
##    plt.plot(calc, calc)
##    # make these tick labels invisible
##    plt.setp(ax2.get_xticklabels(), visible=False)
##
##    # share x and y
##    ax3 = plt.subplot(313, sharex=ax1, sharey=ax1)
##    plt.plot(calc, voltage)
##    plt.xlim(0, 60.0)

##    ax.clear()
##    plt.subplot(2, 1, 1)
##    
##    plt.plot(dt.datetime.now().strftime('%S.%f'), voltage, 'o-')
##    plt.title('calc View')
##    plt.ylabel('calc (V)')
##    plt.xlabel('Time (s)')
##
##    plt.subplot(2, 1, 2)
##    plt.plot(dt.datetime.now().strftime('%S.%f'), AD, '.-')
##    plt.xlabel('time (s)')
##    plt.ylabel('AD')


    plt.grid()

##    plt.figure(2)
##    plt.subplot(312)
##
##    xs.append(dt.datetime.now().strftime('%S.%f'))#('%H:%M:%S'))
##    ys.append(calc)

##    xs = xs[-20:]
##    ys = ys[-20:]

##    ax.clear()
##    ax.plot(xs, ys)
##    
##    plt.xticks(rotation=45, ha='right')
##    plt.subplots_adjust(bottom=0.30)
##    plt.title('calc View')
##    plt.ylabel('calc (V)')
##    plt.xlabel('Time (s)')

##    plt.figure(3)
##    plt.subplot(313)
##
##    plt.plot(dt.datetime.now().strftime('%S.%f'), voltage, color='blue', marker = 'o', linestyle = 'solid')
##
##    plt.grid()
 

while 1:
    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1)
    plt.show()
    
# Set up plot to call animate() function periodically

