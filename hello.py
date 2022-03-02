# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 11:26:57 2022

@author: DR ABIMBOLA OJ
"""
import math
import numpy as np
import matplotlib.pyplot as plt

def velocity_a(t):
    m = 2
    g = 9.8
    C = 0.5
    v = (g*m/C)*(1 - math.exp(-(C/m)*t))
    return(v)

def velocity_n(t2, v1=0, t1=0):
    m = 2
    g = 9.8
    C = 0.5
    v2 = v1+(g-(C/m)*v1)*(t2-t1)
    return(v2)

#print('time',' ', 'velocity_a',' ', 'velocity_n',' ', 'error')

t0 = 0
v0 = 0
x_t = np.arange(0, 50, 0.5)
vel_a = []
vel_n = []
for t in x_t:
    vel_a = np.append(vel_a, velocity_a(t))
    vel_n = np.append(vel_n, velocity_n(t, v0, t0))
    
    #vel_a = velocity_a(t)
    vel_np = velocity_n(t, v0, t0)
    
    #error = vel_n - vel_a
    
    #print(t,' ', vel_a,' ', vel_n,' ', error)
    
    t0 = t
    v0 = vel_np

#print(vel_n)
plt.plot(x_t, vel_a, x_t, vel_n)
plt.grid()

plt.legend(['analytical solution', 'numerical solution'])
plt.xlabel('Time (s)', fontsize = 16)
plt.ylabel('Velocity (m/s)', fontsize = 16)
plt.title('Free Fall Velocity Numerical Simulation', fontsize = 16)
plt.show()
