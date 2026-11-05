#!/usr/bin/python3
#frickeled by sascha.naske@proton.me
import serial

class HP54120B:
	GPIB_ADDRESS = 7
	fd = None
	def __init__(self, gpib_path):
		splitted_path = gpib_path.split('::');
		if splitted_path[0] == "PROLOGIX":
			self.fd = serial.Serial(splitted_path[1], baudrate=921600, timeout=0.5);
			self.fd.write(str.encode("++mode 1\n"))
			self.fd.write(str.encode("++ifc\n"))
			self.fd.write(str.encode("++read_tmo_ms 400\n"))
			self.GPIB_ADDRESS = int(splitted_path[-1]);
		else:
			print("bruuh!\n");
	
	def cmd(self, cmd):
		self.fd.write(str.encode("++addr %d\n" %self.GPIB_ADDRESS))
		self.fd.write(str.encode(cmd + "\n"));
		result = []
		c = 10
		while c > 0:
			lines = self.fd.readlines()
			if len(lines) > 0:
				c = 0
				for c_0 in lines:
					result.append(c_0)
			c-=1
		return result
	def write(self, cmd):
		self.fd.write(str.encode("++addr %d\n" %self.GPIB_ADDRESS))
		self.fd.write(str.encode(cmd + "\n"))
		return
							

	
