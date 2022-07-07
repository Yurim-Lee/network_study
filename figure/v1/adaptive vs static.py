
import matplotlib.pyplot as plt
plt.plot(['0.1%','1%','10%','100%'],[65.37,68.94,74.5,67.1], 'ro-', label = 'Static')
plt.plot(['0.1%','1%','10%','100%'],[72.91,78.01,80.06,79.61], 'b^-', label = 'Adaptive')


plt.xlabel('Data size', fontsize=12)
plt.ylabel('F1 score(%)', fontsize=12)
plt.legend()

plt.show()

