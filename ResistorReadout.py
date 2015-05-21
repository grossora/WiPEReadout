from pylab import *
import numpy as np
from matplotlib.collections import LineCollection
import matplotlib.colors as clr
import matplotlib.cm as cmx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib as mpl

import itertools


#the resistor values
#resvalues = [10000,20000,30000,50000, 70000, 110000,130000,170000]# THIS WORKS  in Ohms
#resvalues = [1000,2000,3000,5000, 7000, 11000,13000,17000,23000,29000]# THIS WORKS  in Ohms
#resvalues = [100,200,300,500, 700, 1100,1300,1700,1900,2300]# THIS WORKS  in Ohms

resvalues = [23000,29000,31000,37000,41000,43000,47000,53000]# THIS is from linda 
##resvalues = [1000,2000,3000,5000, 7000, 11000,13000,17000]# For 8 Wires this is what we would need


eqreslist = []
eqreslistpair = []
Curlist20 = []# expressed in Amps
testvolt = 20.0
	
for L in range(0,len(resvalues)+1):
    for subset in itertools.combinations(resvalues,L):
	eqresA = 0.0
	for res in subset: 
	    eqresA+= 1.0/res
	if eqresA==0: 
	    continue
	eqres = 1/eqresA
	Curlist20.append(testvolt/eqres) 
	eqreslist.append(eqres)
	if len(subset)==2:
	    eqreslistpair.append(eqres)

# if measured at 20 V what is the difference between the closest possible pairs of wire combos
Curlist20, size = sorted(Curlist20), len(Curlist20)
res = [Curlist20[i + 1] - Curlist20[i] for i in xrange(size) if i+1 < size]
print "Current Spread at {0} V ::  MinDiff: {1} microAmps, MaxDiff: {2} microAmps.".format( testvolt, min(res)*1000000.0, max(res)*1000000.0)
print "At a 500 V :: Current through the smallest resistor is {0} Amps, The power dissipated is {1} Watts.".format( min(resvalues), pow(400.0,2)/min(resvalues) )


voltage = np.arange(0,500,0.1)


#Plot all combos
print ' Total combinations ' , len(eqreslist)
for r in eqreslist:
    current = voltage/r*1000# puttin it in milliamps
    plt.plot(voltage,current)
plt.xlabel('Voltage (V)',fontsize='large')
plt.ylabel('Current (mA)')
plt.title('I-V curves for all possible combinations of {0} resistors in parallel'.format(len(resvalues)))
plt.show()

#Plot all pair combos
print ' Total Pair combinations ' ,len(eqreslistpair)
for r in eqreslistpair:
    current = voltage/r*1000# puttin it in milliamps
    plt.plot(voltage,current)
plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')
plt.title('I-V curves for all possible pair combinations of {0} resistors in parallel'.format(len(resvalues)))
plt.show()








