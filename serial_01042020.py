import serial
import matplotlib.pyplot as plt
from config_AD71244 import *
import atexit
import time
import matplotlib.animation as animation
import datetime as dt
from random import randint

import numpy as np



fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

serialArduino = serial.Serial(DEVICE , BAUD_RATE, timeout= TIMEOUT )
time.sleep(1)

##var1 = "S"
##print("enviou s: ")
##serialArduino.write(str.encode(var1))                     # Envia a solicitação para leitura de dados peço AD
##
##time.sleep(1)
##var2 = "C"
##print("enviou c: ")
##
##serialArduino.write(str.encode(var2)) 

##data = serialArduino.readline().decode('ascii')
##print("data: " , data)

def animate(i, xs, ys):

    var1 = "S"
    serialArduino.write(str.encode(var1))                     # Envia a solicitação para leitura de dados peço AD
##    time.sleep(1)
    serialArduino.write(str.encode(var1)) 


##    temp_c = [randint(0,100) for _ in range(1)]  #serialArduino.readline().decode('ascii') #[randint(0,100) for _ in range(1)] #serialArduino.readline().decode('ascii')
    temp_c = serialArduino.readline().decode('ascii') #[randint(0,100) for _ in range(1)] #serialArduino.readline().decode('ascii')
    print("temp_c: " , temp_c)
    print("TEMPO: " , dt.datetime.now().strftime('%S'))
    
    print (type(temp_c))

##    lines = temp_c.split(' ')
##    print("lines:", lines)

##    lines = temp_c.split(' ')
##    for x in lines:
##        st = x.strip()
##        print("lines:", lines)
##        print("st:", st)
##        print("\n")

    lines = temp_c.split(' ')
    a, b, c, d, e = lines
    print("lines:", lines)

    map(int, temp_c.split())
    print("    map(int, temp_c.split()) :",     map(int, temp_c.split()))

    vetor = np.asarray(lines)
    print("vetor:", vetor)
    print("v1:", vetor[3])

    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)
    print("e:", e)


    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%S'))#('%H:%M:%S'))
    ys.append(vetor[3])

    # Limit x and y lists to 20 items
    xs = xs[-10:]
    ys = ys[-10:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('TMP102 Temperature over Time')
    plt.ylabel('Temperature (deg C)')

    time.sleep(0.7)
    
while 1:
    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
    #time.sleep(0.5)
    plt.show()
    
# Set up plot to call animate() function periodically


