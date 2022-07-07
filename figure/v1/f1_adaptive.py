
import matplotlib.pyplot as plt

x = [0,1,2,3,4,5,6]
pro =[86.3,	85.9,	85.42,	86.3,	90.23,	90.93,	91.13]
conventional = [84.56,	84.52,	84.26,	60.1,	60.12,	60.12,	30.1]
f27  = [91.13,	89.98,	80.58,	43.59,	36.25,	36.22,	36.22]

plt.plot(x,pro, 
	color = 'blue',
	marker = 'o',
	linestyle = '-',
	label = 'Proposed-adaptive')
	
plt.plot(x,conventional, 
	color = 'orange',
	marker = '^',
	linestyle = '-',
	label = 'Conventional-adaptive')
	
plt.plot(x,f27, 
	color = 'gray',
	marker = 's',
	linestyle = '-',
	label = 'w/o feature selection')




plt.xlabel('Noise level', fontsize=12)
plt.ylabel('F1 score (%)', fontsize=12)
plt.legend()

plt.show()

