# lattu
#### Straightforward way to control BLE controlled smart bulbs.

# Supported bulbs
I only have Iota light bulb with me so that's the only one supported for now.

It's really easy to add support for your bulbs if you know the GAT commands, have a look at [command maker](iota_command_maker.py).

# Installation
```sh
$ pip install lattu
```

# Example 

```python
>>> from lattu import IotaBulb

>>> my_bulb = IotaBulb('98:7b:f3:37:6a:e7')
>>> my_bulb.connect()

>>> my_bulb.on()
>>> my_bulb.off()

>>>  my_bulb.on('00ff00')  # Green!

>>> my_bulb.color('0000ff')  # Blue!
>>> my_bulb.color('0000ff', 50)  # Blue, but half bright
```

# Thanks
thanks to https://github.com/arijitdasgupta for previous work.
