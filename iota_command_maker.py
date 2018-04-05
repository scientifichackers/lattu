import re


def checksum_gen(packet):
	packetsum = 0
	for i in re.findall('..', packet):
		packetsum += int(i, 16)

	p2 = packetsum + 0xE8

	checksum = (packetsum + 0xE8) & 0xFF
	return (hex(checksum ))

def checksum_gen_color(packet):
	packetsum = 0

	for i in re.findall('..', packet):
		packetsum += int(i, 16)

	p2 = packetsum + 0xE5
	checksum = (packetsum + 0xE5) & 0xFF
	return (hex(checksum ))


def command_gen(operation, color='000000'):
	header = '0x0f0a0d00'
	color = '0x' + color
	on_command = '0x00050000'
	off_command = '0xc8050000'

	if operation == "off":
		mydata = [header, color, on_command]
	elif operation == "on":
		mydata = [header, color, off_command]
	else:
		print('unknown command')
	
	packet = ''.join([i[2:] for i in mydata])[:-2]
	checksum = checksum_gen(packet)
	final_packet = ''.join([i[2:] for i in mydata])
	final_command = final_packet + checksum[2:] + 'ffff'
	return final_command


def command_color_gen(color, brightness):
	color = '0x' + color
	brightness = hex(brightness*2)
	header = '0x0f0d0300'
	#color = '0x000000'
	#brightness = '0xc8'
	padding = '0x000000000000'

	mydata = [header, color, brightness, padding, ]
	
	packet = ''.join([i[2:] for i in mydata])[:-2]
	checksum = checksum_gen_color(packet)
	final_packet = ''.join([i[2:] for i in mydata])
	final_command = final_packet + checksum[2:] + 'ffff'
	return final_command
