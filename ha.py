import paho.mqtt.client as mqtt # Import the MQTT library
import sense_hat
import time
import os
from icons import static_icons

#What the sense Hat is playing
off_state = "turn_off"
state = { "current" : off_state,
          "history" : [],
          "history_index":-1
}

#======= MQTT =======
def on_connect(client, userdata, flags, rc):
  if rc==0:
    client.connected_flag=True #set flag
    print("connected OK")
  else:
    print("Bad connection Returned code=",rc)

# Our "on message" event
def messageFunction (client, userdata, message):
  topic = str(message.topic)
  message = str(message.payload.decode("utf-8"))
  state["current"] = message
  if message <> off_state:
    state["history"].append(message)
    state["history_index"] = len(state["history"])-1
    
ourClient = mqtt.Client("sensehat_mqtt") # Create a MQTT client object
un = open('config_un', 'r').read().replace('\n', '') #TO-DO put in encrypted config
pw = open('config_pw', 'r').read().replace('\n', '') #TO-DO put in encrypted config
ip = open('config_ip', 'r').read().replace('\n', '') #TO-DO put in encrypted config
ourClient.username_pw_set(un, pw) #TO-DO put in encrypted config
ourClient.on_connect=on_connect  #bind call back function
ourClient.connect(ip, 1883) # Connect to the test MQTT broker
ourClient.subscribe("sensehat") # Subscribe to the topic AC_unit
ourClient.on_message = messageFunction # Attach the messageFunction to subscription
ourClient.loop_start() # Start the MQTT client

#======= SenseHat =======
s = sense_hat.SenseHat()
#s.low_light = True

state["history_index"]=len(state["history"])-1
si = static_icons()

def handle_stick(event):
  last_index = len(state["history"])-1
  if last_index == -1:
    state["current"]="sad_logo"
  else:
    if event.action == sense_hat.ACTION_RELEASED:
      # Ignore releases
      return
    elif event.direction == sense_hat.DIRECTION_UP:
      #Turn off
      state["current"]="turn_off"
      state["history_index"]=last_index #reset to last index
    elif event.direction == sense_hat.DIRECTION_DOWN:
      #Show last
      state["current"]=state["history"][last_index]
      state["history_index"]=last_index #reset to last index
    elif event.direction == sense_hat.DIRECTION_RIGHT:
      #Forward in history
      if state["history_index"]<>last_index:
        state["history_index"]=state["history_index"]+1    
        state["current"]=state["history"][state["history_index"]]
    elif event.direction == sense_hat.DIRECTION_LEFT:
      #Back in history
      if state["history_index"]<>0:
        if state["current"]=="turn_off": #if it is in the off state, show the last
          state["current"]=state["history"][last_index]
        else:               
          state["history_index"]=state["history_index"]-1
          state["current"]=state["history"][state["history_index"]]

keep_going = True
while keep_going: 
  try:
    parts = state["current"].split(" ")
    s.set_pixels(getattr(si, parts[0])())
    if len(parts) > 1:
      if parts[1] == "flash":
        time.sleep(.5)
        s.set_pixels(getattr(si, "turn_off")())
        time.sleep(.5)
    #Handle click at any time
    events = s.stick.get_events()
    if events:
      for event in events:
        handle_stick(event)
    else:
      moved = False
  except Exception as e:     # most generic exception you can catch
    print str(e)
