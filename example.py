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








#print(command_gen('off'))


"""
x = my_bulb.connecter()
time.sleep(1)
x.sendline('char-write-req 0x002b 0f0a0d000000000005000013ffff')
time.sleep(1)
x.sendline('char-write-req 0x002b 0f0a0d00ffffffc8050000d8ffff')
"""