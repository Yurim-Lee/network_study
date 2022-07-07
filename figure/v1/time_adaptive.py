
import matplotlib.pyplot as plt

x = [0,1,2,3,4,5,6]
pro =[0.25,0.54,	0.38,	0.25,	0.26,	0.26,	0.27]
conventional = [0.3,0.39,0.6,0.43,0.41,0.39,0.41]
f27  = [0.45,0.66,0.45,0.44,0.44,0.41,0.4]

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
plt.ylabel('Latency (s)', fontsize=12)
plt.legend()

plt.show()

