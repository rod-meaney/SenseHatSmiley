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
          "mode":"menu",
          "menu_item":0
}

menu = [["?", "Explain menu"],
        ["1", "Run smiley counter"],
        ["2", "Display smiley totals"],
        ["3", "Reset count"],
        ["4", "Quit"],
        ["5", "Explain smiley counter"]
]

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

def add_sad():
    R = red
    O = nothing
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

def add_middle():
    O = nothing
    A = amber
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

def add_input(input_type):
    state["today_"+input_type] += 1
    state["week_"+input_type] += 1
    state["month_"+input_type] += 1

def handle_stick_menu(event):
    if event.action == sense_hat.ACTION_RELEASED:
        # Ignore releases
        return
    elif event.direction == sense_hat.DIRECTION_UP:
        if state["menu_item"] == 0:
            state["menu_item"] = len(menu)-1
        else:
            state["menu_item"] -= 1
    elif event.direction == sense_hat.DIRECTION_DOWN:
        if state["menu_item"] == len(menu)-1:
            state["menu_item"] = 0
        else:
            state["menu_item"] += 1
    elif event.direction == sense_hat.DIRECTION_RIGHT:
        if state["menu_item"] == 0:
            s.show_message("up: Menu item up, down: Menu item Down, < Describe menu item, > Activate menu item")
        elif state["menu_item"] == 1:
            state["mode"] = "running"
        elif state["menu_item"] == 2:
            s.show_message("Happy: %d" % state["today_happy"], text_colour=green)
            time.sleep(1)
            s.show_message("Sad: %d" % state["today_sad"], text_colour=red)
            time.sleep(1)
            s.show_message("Ambivelant: %d" % state["today_middle"], text_colour=amber)
            time.sleep(1)
        elif state["menu_item"] == 3:
            state["today_happy"] = 0
            state["today_sad"] = 0
            state["today_middle"] = 0
            s.show_message("Today reset")
        elif state["menu_item"] == 4:
            s.set_pixels(turn_off())
            quit()
        elif state["menu_item"] == 5:
            s.show_message("up: add happy, down: add sad, < main menu, > add ambivelant")                                
        
    elif event.direction == sense_hat.DIRECTION_LEFT:
        s.show_message(menu[state["menu_item"]][1])

def handle_stick_running(event):
    if event.action == sense_hat.ACTION_RELEASED:
        # Ignore releases
        return
    elif event.direction == sense_hat.DIRECTION_UP:
        s.set_pixels(add_happy())
        add_input("happy")
        time.sleep(state["add_wait_time"])
    elif event.direction == sense_hat.DIRECTION_DOWN:
        s.set_pixels(add_sad())
        add_input("sad")
        time.sleep(state["add_wait_time"])
    elif event.direction == sense_hat.DIRECTION_RIGHT:
        s.set_pixels(add_middle())
        add_input("middle")
        time.sleep(state["add_wait_time"])
    elif event.direction == sense_hat.DIRECTION_LEFT:
        state["mode"] = "menu"
        state["menu_item"] = 0

images = [happy_logo, sad_logo, middle_logo]
count = 0
keep_going = True
while keep_going: 
    if state["mode"] == "running":
        if (state["today_happy"] > state["today_sad"]) and (state["today_happy"]>state["today_middle"]):
            s.set_pixels(happy_logo())
        elif (state["today_sad"] > state["today_happy"]) and (state["today_sad"]>state["today_middle"]):
            s.set_pixels(sad_logo())
        else:
            s.set_pixels(middle_logo())
    if state["mode"] == "menu":    
        s.show_letter(menu[state["menu_item"]][0], text_colour=blue)

    # Handle one click at a time
    event = s.stick.wait_for_event(emptybuffer=True)
    
    #for event in s.stick.get_events():
    if state["mode"] == "running":
        handle_stick_running(event)
    elif state["mode"] == "menu":
        handle_stick_menu(event)