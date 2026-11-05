#!/usr/bin/python
#frickeled by sascha.naske@proton.me

import time
import math
#from matplotlib import pyplot
#from pylab import *
import numpy
#from numpy import arange
import matplotlib.pyplot as plt
import struct
import skrf as rf
#plt.xkcd();
from hp54120b import *

def main():

#	figure(figsize = (8,6), facecolor='white')
	scope = HP54120B('PROLOGIX::/dev/ttyUSB2::GPIB::16')
#	scope.cmd("++ifc");
	print("boop")
#	scope.cmd("++spoll");
#	scope.cmd("++loc");
	time.sleep(1);
#	idstring = scope.cmd("*idn?")
#	idstring = scope.cmd("++read eoi")
#	print(idstring)
#	time.sleep(1);
#	scope.write(":CHANNEL1:RANGE:40MV\n");
#	scope.write("*RST");
#	scope.write(":autoscale");
	scope.write(":acquire:type average");
	scope.write(":acquire:count 4");
	scope.write(":acquire:points 8192");
	scope.write(":acquire:complete 90");
	scope.write(":tim:range 1000ps");
	scope.write(":disp:grat grid");
	scope.write(":DIGITIZE CHANNEL1 ");

#	scope.write(":WAIT ");
#	scope.write(":VIEW CHAENNEL1 ");
#	scope.write(":DIGITIZE:CHANNEL2");
#	scope.write(":DIGITIZE:CHANNEL3");
#	scope.write(":DIGITIZE:CHANNEL4");
#	time.sleep(3);
#	time.sleep(1);
#	time.sleep(3)
	res = scope.cmd(":waveform:format asc");
	for i in range(0,1):
		scope.write(":DIGITIZE CHANNEL1 ");
		scope.write(":WAV:SOURCE WMEMORY1");
		res = scope.cmd(":waveform:preamble?");
		print(res)
		res1 = scope.cmd(":waveform:data?");
		print(res)
		scope.write(":DIGITIZE CHANNEL2 ");
		scope.write(":WAV:SOURCE WMEMORY2");
		res = scope.cmd(":waveform:preamble?");
		print(res)
		res2 = scope.cmd(":waveform:data?");
		print(res)
		scope.write(":DIGITIZE CHANNEL3 ");
		scope.write(":WAV:SOURCE WMEMORY3");
		res = scope.cmd(":waveform:preamble?");
		print(res)
		res3 = scope.cmd(":waveform:data?");
		print(res)
		scope.write(":DIGITIZE CHANNEL4 ");
		scope.write(":WAV:SOURCE WMEMORY4");
		res = scope.cmd(":waveform:preamble?");
		print(res)
		res4 = scope.cmd(":waveform:data?");
		print(res)
	res1 = str(res1)
	res1 = res1.split(',')
	for v in res1[1:-1]:
		print(float(v)/16384.0)
	res1 = [(float(v)/16384.0 - 1.0) * 2.0 for v in res1[1:-1]]
	res2 = str(res2)
	res2 = res2.split(',')
	for v in res2[1:-1]:
		print(float(v)/16384.0)
	res2 = [(float(v)/16384.0 - 1.0) * 1.0 for v in res2[1:-1]]
	res3 = str(res3)
	res3 = res3.split(',')
	for v in res3[1:-1]:
		print(float(v)/16384.0)
	res3 = [float(v)/16384.0 - 1.0 for v in res3[1:-1]]
	res4 = str(res4)
	res4 = res4.split(',')
	for v in res4[1:-1]:
		print(float(v)/16384.0)
	res4 = [float(v)/16384.0 - 1.0 for v in res4[1:-1]]
	diff1 = numpy.diff(res1)
#	for s in res:
#		u = struct.unpack("B", s)
#		print(u)
#	for f in u:
#		print(float(int(f)))
	plt.style.use('dark_background')
	fig, ax = plt.subplots(1);
	t_data1 = numpy.linspace(0.0, len(res1) * 1.0 , len(res1));
	t_datad1 = numpy.linspace(0.0, len(diff1) * 1.0 , len(diff1));
	t_data2 = numpy.linspace(0.0, len(res2) * 1.0 , len(res2));
	t_data3 = numpy.linspace(0.0, len(res3) * 1.0 , len(res3));
	t_data4 = numpy.linspace(0.0, len(res4) * 1.0 , len(res4));
	#t_data = numpy.linspace(0.0, len(res1) * 5.0 ));
	ax.scatter(t_data1, res1, label="Channel #1", color="red", alpha=0.5)
#	ax.scatter(t_data2, res2, label="Channel #2", color="green")
#	ax.scatter(t_data3, res3, label="Channel #3", color="green", alpha=0.5)
#	ax.scatter(t_data4, res4, label="Channel #4", color="blue", alpha=0.5)
	ax.set_xlabel('Time (ps)')
	ax.set_ylabel('Voltage (V)')
	plt.legend(loc="upper left")
#	ax[1].plot(t_data, res1)
	plt.show()
#	c_data = []
if __name__ == "__main__":
    main()
