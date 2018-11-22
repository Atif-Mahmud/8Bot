import logging

import serial

SERIAL_PORT = "COM4"
SERIAL_BAUDRATE = 9600

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("Serial")

def scale(x, inLow, inHigh, outLow, outHigh):
	return (x - inLow) * (outHigh - outLow) / (inHigh - inLow) + outLow

def clamp(x, low, high):
	return max(low, min(high, x))

def scale_clamp(x, inLow, inHigh, outLow, outHigh):
	return clamp(scale(x, inLow, inHigh, outLow, outHigh), outLow, outHigh)

logger.debug("Serial: Attempting connection at (\"%s\", %d)" % (SERIAL_PORT, SERIAL_BAUDRATE))
s = serial.Serial(SERIAL_PORT, SERIAL_BAUDRATE, timeout=5)
logger.info("Serial: Connected.")

def get_next_message():
	input_ = input(">")
	input_ = "".join(input_.split()) # Remove whitespace

	if input_ == "":
		return b"M\x00"

	if input_ == "w":
		return b"M" + bytes([0b10101010])
	if input_ == "s":
		return b"M" + bytes([0b01010101])
	if input_ == "a":
		return b"M" + bytes([0b01011010])
	if input_ == "d":
		return b"M" + bytes([0b10100101])
	if input_ == "q":
		return b"M" + bytes([0b01100110])
	if input_ == "e":
		return b"M" + bytes([0b10011001])

	if input_ == "S":
		return b"S0"

	if ord("0") <= ord(input_[0]) <= ord("9"):
		speed = int(input_[0]) * 32
		speed = min(speed, 255)
		return (b"A" + bytes([speed])
			  + b"B" + bytes([speed]))

	if not input_[0].isupper():
		logger.error("Invalid command!")
		return

	if input_[1] in ("x", "X"): # Hex
		dataByte = int(input_[2:4], base=16)
	elif input_[1] in ("b", "B"): # Binary
		dataByte = int(input_[2:10], base=2)
	else: # Decimal
		dataByte = int(input_[1:])

	if dataByte > 255 or dataByte < 0:
		logger.error("Data byte out of range!")
		return

	return bytes([ord(input_[0]), dataByte])

while True:
	message = get_next_message()
	if message:
		logger.debug("Sending message: %s" % message)
		s.write(message)
