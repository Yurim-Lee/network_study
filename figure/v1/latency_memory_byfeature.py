
import matplotlib.pyplot as plt

x = [0,1,2,3,4,5,6]
latency = [0.278625417,0.297144,0.308444567,0.408176083,0.428257467,
0.449277117,0.465575533]
memory = [1961,2429,2885,5248,7996,8922,12663]

fig1, ax1 = plt.subplots()
ax1.plot(x, latency, 
	color = 'blue',
	marker = 'o',
	linestyle = '-',
	label = 'Latency')
ax1.legend(loc='upper left')

ax2 = ax1.twinx()
ax2.plot(x,memory, 
	color = 'orange',
	marker = '^',
	linestyle = '-',
	label = 'Memory usage')
ax2.legend(loc='lower right')
ax1.set_ylabel('Latency (s)', fontsize=12)
ax2.set_ylabel('Memory usage (KB)', fontsize=12)

plt.xlabel('Number of features', fontsize=12)


plt.show()

