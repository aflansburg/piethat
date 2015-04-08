# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 16:32:12 2015

@author: abram
"""
import sys, os
from pylab import savefig
from matplotlib import pyplot as plt
import numpy as np
"""
"""

try:
	sys.argv[1]
except IndexError:
	print("""Please define the path. Ex: "python interactive_MIR_pieChart.py /users/yourName/yourPath" """)
	exit()
else:
	file_path = sys.argv[1]
filename = raw_input('Please enter a file name. File will be saved with this name to the path ' + file_path + ":  ")
print("PIE CHARTS ARE GREAT")
print("")
print("This script requires a minimum of 2 slices.")
slices = []
sizes = []
i = 0
i = int(input('Number of slices: '))
if i > 15:
    print("Warning: More than 15 slices may cause labels to become unreadable!")
elif i < 2:
	sys.exit("ERROR: You need more than 1 slice. Otherwise, what's the point?")
for i in range (0,i):
    slices.append(raw_input('Slice name #%d: ' % (i+1)))
    sizes.append(input('Slice #%d size: ' %(i+1)))
if sum(sizes) > 100:
    print("!!! FYI: Sizes are greater than 100 !!!")
location = file_path
savelocation = location + filename
print("These are the slices: %s" % slices)
print("These are the sizes: %s" % sizes)

cmap = plt.cm.Pastel2
colors = cmap(np.linspace(0., 1., len(slices)))
plt.rcParams['patch.edgecolor'] = 'white'
plt.rcParams['lines.linewidth'] = 4
plt.pie(sizes, labels=slices, colors = colors, shadow = False, startangle=90, autopct='%1.f%%', radius=0.5)
plt.axis('equal')
# plt.tight_layout()
savefig(savelocation, dpi=225, bbox_inches='tight')
os.system('open ' + location + filename + '.png')