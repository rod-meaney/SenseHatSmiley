import sense_hat
import time

s = sense_hat.SenseHat()
#s.low_light = True

state = { "today_happy" : 0,
          "today_sad" : 0,
          "today_middle" : 0,
          "week_happy" : 0,
          "week_sad" : 0,
          "week_middle" : 0,
          "month_happy" : 0,
          "month_sad" : 0,
          "month_middle" : 0,
          "add_wait_time": 2,
          "mode":"menu"
}

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
amber = (255,140,0)
nothing = (0,0,0)
pink = (255,105, 180)

def turn_off():
    O = nothing
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

def menu_logo():
    B = blue
    O = nothing
    logo = [
    O, O, O, B, B, O, O, O,
    O, O, B, O, O, B, O, O,
    O, B, O, O, O, O, B, O,
    O, O, O, O, O, B, O, O,
    O, O, O, B, B, O, O, O,
    O, O, O, B, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, B, O, O, O, O,
    ]
    return logo

def happy_logo():
    G = green
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, G, O, O, G, O, O,
    O, G, G, O, O, G, G, O,
    O, O, O, O, O, O, O, O,
    G, O, O, O, O, O, O, G,
    O, G, O, O, O, O, G, O,
    O, O, G, G, G, G, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def add_happy():
    G = green
    O = nothing
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

def sad_logo():
    R = red
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, R, O, O, O, O, R, O,
    O, R, R, O, O, R, R, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, R, R, R, R, O, O,
    O, R, O, O, O, O, R, O,
    R, O, O, O, O, O, O, R,
    ]
    return logo

def middle_logo():
    A = amber
    O = nothing
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

def add_input(input_type):
    state["today_"+input_type] += 1
    state["week_"+input_type] += 1
    state["month_"+input_type] += 1

def handle_mult_input():
    state["input_happening"] = True
    time.sleep(1.5)
    state["input_happening"] = False    

def handle_stick_menu(event):
    if event.action == sense_hat.ACTION_RELEASED:
        # Ignore releases
        return
    elif event.direction == sense_hat.DIRECTION_UP:
        return
    elif event.direction == sense_hat.DIRECTION_DOWN:
        return
    elif event.direction == sense_hat.DIRECTION_RIGHT:
        state["mode"] = "running"
    elif event.direction == sense_hat.DIRECTION_LEFT:
        s.set_pixels(turn_off())
        quit()

def handle_stick_running(event):
    if event.action == sense_hat.ACTION_RELEASED:
        # Ignore releases
        return
    elif event.direction == sense_hat.DIRECTION_UP:
        s.set_pixels(add_happy())
        add_input("happy")
        time.sleep(state["add_wait_time"])
        #handle_mult_input()
    elif event.direction == sense_hat.DIRECTION_DOWN:
        return
    elif event.direction == sense_hat.DIRECTION_RIGHT:
        return
    elif event.direction == sense_hat.DIRECTION_LEFT:
        state["mode"] = "menu"

images = [happy_logo, sad_logo, middle_logo]
count = 0
keep_going = True
while keep_going: 
    if state["mode"] == "running":
        s.set_pixels(happy_logo())
    if state["mode"] == "menu":    
        s.set_pixels(menu_logo())

    # Handle one click at a time
    event = s.stick.wait_for_event(emptybuffer=True)
    
    #for event in s.stick.get_events():
    if state["mode"] == "running":
        handle_stick_running(event)
    elif state["mode"] == "menu":
        handle_stick_menu(event)