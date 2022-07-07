
import matplotlib.pyplot as plt

x = [0,1,2,3,4,5,6]
prof4 = [72.8,	73.25,	78.22,	86.3,	90.23,	90.93,	91.13]
prof11 = [86.3,	85.9,	85.42,	73.95,	53.78,	36.22,	36.22]
conf4 = [60.1,	60.1,	60.1,	60.1,	60.12,	60.12,	30.1]
conf11 = [84.56,	84.52,	84.26,	84.32,	81.84,	81.28,	80.88]


plt.plot(x,prof4, 
	color = 'blue',
	marker = 'o',
	linestyle = '-',
	label = 'FSFG (f4)')
	
plt.plot(x,prof11, 
	color = 'blueviolet',
	marker = 's',
	linestyle = '-',
	label = 'FSFG (f11)')
	
plt.plot(x,conf4, 
	color = 'gray',
	marker = 'X',
	linestyle = '--',
	label = 'Conventional (f4)')

plt.plot(x,conf11, 
	color = 'black',
	marker = 'P',
	linestyle = '--',
	label = 'Conventional (f11)')


plt.xlabel('Noise level', fontsize=12)
plt.ylabel('F1 score(%)', fontsize=12)
plt.legend()

plt.show()

