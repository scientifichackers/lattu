# lattu
straightforward way to control BLE controlled smart bulbs

# Supported bulbs
I only have Iota light bulb with me so that's the only one supported for now.
It's really easy to add support for your bulbs if you know the GAT commands, have a look at lattu.py
# Example 

from lattu import IotaBulb
import time

my_bulb = IotaBulb('98:7b:f3:37:6a:e7')
my_bulb.connect()

my_bulb.on()
time.sleep(1)

my_bulb.off()
time.sleep(1)

my_bulb.on('00ff00') # On support color 
time.sleep(0.5)

my_bulb.color('ffffff')
time.sleep(0.5)

my_bulb.color('ffffff', 50) # color support brightness
