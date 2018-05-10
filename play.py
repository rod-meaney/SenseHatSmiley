#from sense_hat import SenseHat
import math

#s = SenseHat()
#values must be between 0 and 16
state = { "today_happy" : 40,
          "today_sad" : 6,
          "today_middle" : 12}

def bar_graph(r,y,g):
    G = (0, 255, 0)
    Y = (255, 255, 0)
    R = (255, 0, 0)
    N = (0,0,0)

    lista = [r,y,g]
    div = (math.trunc(max(lista)/16)+1)*16 #Largest divisor of 16

    r=int(round((r*16)/div)) 
    y=int(round((y*16)/div))
    g=int(round((g*16)/div))

    display = []
    sad=[57,56,49,48,41,40,33,32,25,24,17,16,9,8,1,0]
    meh=[60,59,52,51,44,43,36,35,28,27,20,19,12,11,4,3]
    happy=[63,62,55,54,47,46,39,38,31,30,23,22,15,14,7,6]
    #Set to blank
    for x in range (0,64):
        display.append(N)
    #sad
    for x in range (0,r):
        display[sad[x]] = R
    #meh
    for x in range (0,y):
        display[meh[x]] = Y
    #happy
    for x in range (0,g):
        display[happy[x]] = G        
    return display

#new_logo = update_logo(state["today_sad"],state["today_middle"],state["today_happy"])
import time
print time.time() % 60


#keep_going = True
#while keep_going: 
#    s.set_pixels(update_logo(state["today_sad"],state["today_middle"],state["today_happy"]))
