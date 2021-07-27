# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 09:28:08 2021

@author: sahooa
"""
%reset -f
import numpy as np
import matplotlib.pyplot as plt

with open('./output/airfoil_normals.txt') as airfoilGeometry:
    data = airfoilGeometry.readlines()
airfoilcoord = []
for line in data:
    temp = line.split()
    temp = temp = list(map(float, temp))
    airfoilcoord.append(temp)
    
x = []
y = []
for i in range(0, len(airfoilcoord), 1):
    x.append(airfoilcoord[i][0])
    y.append(airfoilcoord[i][1])
    
with open('./output/bl_quantities.txt') as blQuantities:
    data2 = blQuantities.readlines()
blquants = []
for line in data2:
    temp = line.split()
    temp = temp = list(map(float, temp))
    blquants.append(temp)
    
bl_x = []
bl_y = []
bl_z = []
delta = []
delta_1 = []
delta_2 = []
delta_3 = []
for i in range(0, len(blquants), 1):
    bl_x.append(blquants[i][0])
    bl_y.append(blquants[i][1])
    bl_z.append(blquants[i][2])
    delta.append(blquants[i][3])
    delta_1.append(blquants[i][4])
    delta_2.append(blquants[i][5])
    delta_3.append(blquants[i][6])

#%% Plotting    
plt.figure(1)
plt.title('AoA=0, Re=6e6')
plt.xlabel('x')
plt.ylabel('y')
# plt.ylim(-0.1,0.1)
# plt.xlim(-0.1,1.1)
plt.plot(x[:], y[:], 'k', label="NACA 0012")
plt.plot(bl_x[:], bl_y[:], '*b', label="BL Vorticity definition")
plt.legend(loc="best")
plt.show()

plt.figure(2)
plt.title('AoA=0, Re=6e6')
plt.xlabel('x')
# plt.ylabel('${\delta}_{1}$')
# plt.ylim(-0.1,0.1)
# plt.xlim(-0.1,1.1)
plt.plot(bl_x[:], delta_1[:], 'k', label=r'${\delta}^{*}$')
plt.plot(bl_x[:], delta_2[:], 'b', label=r'$\theta$')
plt.plot(bl_x[:], delta_3[:], 'r', label=r'${\delta}_{k}$')
plt.legend(loc="best")
plt.show()
        
    