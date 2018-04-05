# Python Class for controlling ble based light bulbs
import pexpect
import time
from time import gmtime, strftime
from iota_command_maker import command_color_gen, command_gen



class Bulb:
	"Common base class for all the bulbs"

	def __init__(self, mac_address):
		self.child = pexpect.spawn("gatttool -I")
		self.mac_address = mac_address
	
	def connect(self):
		self.child.sendline("connect {0}".format(self.mac_address))
		self.child.expect("Connection successful", timeout=5)
		#return self.child

	def write(self, handle, command):
		full_command = "char-write-req %s %s" % (handle,command)
		self.child.sendline(full_command)
		self.child.expect("Characteristic value was written successfully", timeout=5)


class IotaBulb(Bulb):
	"Inherited class for Iota Light bulb"

	def __init__(self, mac_address, handle='0x002b'):
		super().__init__(mac_address)
		self.handle = handle


	def on(self, color='ffffff'):
		"""Turns the bulb on, accept color in ffffff format: bulb.on('ffffff') """
		command = command_gen('on', color)
		self.write(self.handle, command)

	def off(self):
		""" Turns the bulb off """
		command = command_gen('off')
		self.write(self.handle, command)

	def color(self, color, brightness=100):
		""" Change the color and brightness, brightness is optional: bulb.color('ffffff', 50)
		Note: This bulb only support brightness values from 8 to 100  """
		if brightness < 8:
			brightness = 8
			# print('This bulb only support brightness value greater than 7')
		command = command_color_gen(color, brightness)
		self.write(self.handle, command)