import math
class static_icons:
    green = (0, 255, 0)
    light_green = (198,247,51)
    yellow = (255, 255, 0)
    blue = (0, 0, 255)
    bright_blue = (111,225,226)
    red = (255, 0, 0)
    light_red = (255, 111, 111)
    white = (255,255,255)
    amber = (255,140,0)
    nothing = (0,0,0)
    pink = (255,105, 180) 
    light_pink = (249,157, 209) 
    purple = (155,0,255)
    light_purple = (249,132,249)

    def turn_off(self):
        O = self.nothing
        logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def bin(self):
        O = self.nothing
        B = self.blue
        logo = [
        O, B, B, B, B, B, B, O,
        B, B, O, O, O, O, B, B,
        O, B, O, B, B, O, B, O,
        O, B, O, B, B, O, B, O,
        O, B, O, B, B, O, B, O,
        O, B, O, B, B, O, B, O,
        O, O, B, O, O, B, O, O,
        O, O, B, B, B, B, O, O,
        ]
        return logo

    def phone(self):
        O = self.nothing
        R = self.red
        L = self.light_red
        W = self.white
        logo = [
        O, O, O, O, O, O, O, O,
        O, L, L, L, L, L, L, O,
        L, L, L, L, L, L, L, L,
        L, L, W, W, W, W, L, L,
        L, L, W, R, R, W, L, L,
        O, W, W, R, R, W, W, O,
        R, R, R, R, R, R, R, R,
        R, R, R, R, R, R, R, R,
        ]
        return logo

    def c_scene(self):
        Y = self.yellow
        B = self.bright_blue
        P = self.light_pink
        G = self.green
        R = self.red
        logo = [
        Y, Y, B, Y, B, B, B, B,
        Y, Y, B, B, B, B, B, B,
        B, B, B, Y, B, B, B, B,
        R, Y, R, R, R, R, R, R, 
        R, R, R, R, R, P, R, R, 
        R, R, R, R, R, G, R, R, 
        R, R, R, R, R, G, R, R, 
        G, G, G, G, G, G, G, G, 
        ]
        return logo

    def c_building(self):
        R = self.red
        Y = self.yellow
        A = self.amber
        G = self.light_green
        O = self.nothing
        logo = [
        O, O, O, O, O, O, O, O,
        O, O, R, R, R, R, O, O, 
        R, R, A, A, A, A, R, R,
        R, A, Y, Y, Y, Y, A, R,
        R, A, Y, G, G, Y, A, R,
        R, A, Y, G, G, Y, A, R,
        R, A, Y, G, G, Y, A, R,
        R, A, Y, G, G, Y, A, R,
        ]
        return logo

    def c_pink(self):
        P = self.light_pink
        M = self.purple
        logo = [
        P, P, P, P, P, P, P, P,
        P, M, M, M, M, M, M, P,
        P, M, P, P, P, P, M, P,
        P, M, P, M, M, P, M, P,
        P, M, P, M, M, P, M, P,
        P, M, P, M, M, P, M, P,
        P, M, P, M, M, P, M, P,
        P, M, P, M, M, P, M, P,
        ]
        return logo

    def c_heart(self):
        P = self.purple
        O = self.nothing
        logo = [
        P, P, P, O, O, P, P, P,
        P, P, P, P, P, P, P, P,
        P, P, P, P, P, P, P, P,
        O, P, P, P, P, P, P, O,
        O, O, P, P, P, P, O, O,
        O, O, O, P, P, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def happy_logo(self):
        G = self.green
        O = self.nothing
        logo = [
        O, O, O, O, O, O, O, O,
        O, G, G, O, O, G, G, O,
        O, G, G, O, O, G, G, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, G, O, O, O, O, G, O,
        O, O, G, G, G, G, O, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def happy_less_logo(self):
        G = self.green
        O = self.nothing
        logo = [
        O, O, O, O, O, O, O, O,
        O, G, G, O, O, G, G, O,
        O, G, G, O, O, G, G, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, G, G, G, G, G, G, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def add_happy(self):
        G = self.green
        O = self.nothing
        logo = [
        O, G, O, O, O, O, O, O,
        G, G, G, O, O, O, O, O,
        O, G, O, O, G, O, G, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, G, O, O,
        O, O, O, G, O, O, O, G,
        O, O, O, O, G, G, G, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def sad_logo(self):
        R = self.red
        O = self.nothing
        logo = [
        O, O, O, O, O, O, O, O,
        O, R, O, O, O, O, R, O,
        O, R, R, O, O, R, R, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, R, R, R, R, O, O,
        O, R, O, O, O, O, R, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def sad_less_logo(self):
        R = self.red
        O = self.nothing
        logo = [
        O, O, O, O, O, O, O, O,
        O, R, O, O, O, O, R, O,
        O, R, R, O, O, R, R, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, R, R, R, R, R, R, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def add_sad(self):
        R = self.red
        O = self.nothing
        logo = [
        O, R, O, O, O, O, O, O,
        R, R, R, O, O, O, O, O,
        O, R, O, O, R, O, R, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, R, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, R, R, R, O,
        O, O, O, R, O, O, O, R,
        ]
        return logo

    def middle_logo(self):
        A = self.amber
        O = self.nothing
        logo = [
        O, O, O, O, O, O, O, O,
        O, A, A, O, O, A, A, O,
        O, A, A, O, O, A, A, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, A, A, A, A, A, A, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def add_middle(self):
        O = self.nothing
        A = self.amber
        logo = [
        O, A, O, O, O, O, O, O,
        A, A, A, O, O, O, O, O,
        O, A, O, O, A, O, A, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, A, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, A, A, A, A, A,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def bar_graph(self,r,y,g):
        G = (0, 255, 0)
        Y = (255, 255, 0)
        R = (255, 0, 0)
        N = (0,0,0)

        lista = [r,y,g]
        div = (math.trunc(max(lista)/16)+1) #Largest divisor of 16

        r=int(round((r)/div)) 
        y=int(round((y)/div))
        g=int(round((g)/div))

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
