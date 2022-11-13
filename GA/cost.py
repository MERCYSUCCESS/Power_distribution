import numpy as np
import matplotlib.pyplot as plt
 
# set width of bar
barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))
 
# set height of bar
IT = [12, 30, 1, 8, 22]
# #CSE = [29, 3, 24, 25, 17]
 
# Set position of bar on X axis
br1 = np.arange(len(IT))
x = [x + barWidth for x in br1]
y = [x + barWidth for x in br1]
 
# Make the plot
plt.plot(x, y, color ='r')
# plt.bar(br2, ECE, color ='g', width = barWidth,
#         edgecolor ='grey', label ='ECE')
# plt.bar(br3, CSE, color ='b', width = barWidth,
#         edgecolor ='grey', label ='CSE')
 
# Adding Xticks
plt.xlabel('Transmission Line', fontweight ='bold')
plt.ylabel('Cost of Power', fontweight ='bold')

plt.title("Power Distribution")
plt.legend()
plt.show()