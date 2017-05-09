#!/usr/bin/env python
import numpy as np
from math import * 

x=[1]
t=[0.0]
v=[0.0]
k=1.0
m=1.0
mi=0.003
gT=9.8
gL=1.625
dt=0.001
a=[0.0]
p=[0]

while (t[-1]<=60):
	if (x[-1]<0 and x[-2]>0):
		p.append(t[-1])
	t.append(t[-1]+dt)
	x.append(x[-1]+v[-1]*dt +0.5*a[-1]*dt**2)
	a.append((k/m)*(-x[-1])+((-np.sign(v[-1]))*mi*gT))	
	v.append(v[-1]+0.5*(a[-2]+a[-1])*dt)

print p
plt.figure(figsize=(8,5), dpi=100)
#plt.axis([0,60,-1, 1])
ax=plt.gca()
ax.spines ["right"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["bottom"].set_position(("data", 0))
ax.spines["left"].set_position(("data", 0))
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
ax.autoscale()
#plt.rc('text', usetex=True)
#plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
#plt.xlabel(r'\textnormal{Posi\c{c}\~{a}o} (m)')
#plt.ylabel(r'\textnormal{Velocidade (m/s)')

#plt.title(r'\textnormal{Oscila\c{c}\~{a}o com Atrito }', fontsize=14)

#plt.plot (t, x , '-g', linewidth=1)
#plt.plot (t, v, '-c', linewidth=1) 
#plt.legend(loc='upper right')
#plt.savefig("p.pdf", dpi=96)
#plt.show()	
