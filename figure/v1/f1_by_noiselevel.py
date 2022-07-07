
import matplotlib.pyplot as plt

x = [0,1,2,3,4,5,6]
f4 = [72.8,73.25,78.22,86.3,90.23,90.93,91.13]
f5 = [72.8,	78.15,	78.17,	85.99,	89.49,	89.81,	89.94]
f6 = [73.11,	78.22,	78.09,	85.42,	83.87,	83.09,	80.83]
f11 = [73.34,	78.18,	75.08,	73.96,	75.48,	60.73,	43.08]
f17 = [73.36,	77.84,	78.19,	53.79,	40.73,	34.44,	36.25]
f19 = [73.38,	75.21,	78.2,	36.22,	34.52,	33.99,	36.22]
f27 = [73.91,	75.08,	77.6,	36.22,	34.02,	33.99,	36.22]




plt.plot(x,f4, 
	color = 'blue',
	marker = 'o',
	linestyle = '-',
	label = 'f4')
	
plt.plot(x,f5, 
	color = 'orange',
	marker = '^',
	linestyle = '-',
	label = 'f5')
	
plt.plot(x,f6, 
	color = 'gray',
	marker = 's',
	linestyle = '-',
	label = 'f6')

plt.plot(x,f11, 
	color = 'cyan',
	marker = 'v',
	linestyle = '-',
	label = 'f11')
	
plt.plot(x,f17, 
	color = 'yellow',
	marker = '*',
	linestyle = '-',
	label = 'f17')
	
plt.plot(x,f19, 
	color = 'black',
	marker = 'X',
	linestyle = '-',
	label = 'f19')
	
plt.plot(x,f27, 
	color = 'magenta',
	marker = 'D',
	linestyle = '-',
	label = 'f27')


plt.xlabel('Noise level', fontsize=12)
plt.ylabel('F1 score(%)', fontsize=12)
plt.legend()

plt.show()

