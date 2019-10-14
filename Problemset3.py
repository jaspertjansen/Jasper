# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 15:30:35 2019

@author: jansen
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



#constants
L = 100 * 10**(-9) #m
N= 100
T=1000 #K
mu=1.66053904*10**(-27) #kg
kb=1.38064852*10**(-23) #m^2 kg s^(-2) K^(-1)
deltat=L/5000 #s
m = 32*mu #mass of oxygen molecule
t=1000

momentum=0



positions = np.random.rand(N,3)*L #positions[N] gives x,y,z coordinate of 
                                  #the Nth particle. N goes from 0 to 99
#The box goes from 0 to L in all directions
                                  
all_positions=[]
all_positions.append(positions)


for i in range(100): #This should be 100 for part A and 1000 for part B
    #Because 100 is good to see the plot, but too few to do part B

    #b

    velocitiesx=np.random.normal(0,np.sqrt((kb*T)/m),N) #velocitiesx[0] gives the
                                                        #x-speed of the Nth particle
    velocitiesy=np.random.normal(0,np.sqrt((kb*T)/m),N)
    velocitiesz=np.random.normal(0,np.sqrt((kb*T)/m),N)                                                   
                                                       
#    print("The average x-speed is:", np.mean(velocitiesx), "m/s")
#    print("The average y-speed is:", np.mean(velocitiesy), "m/s")
#    print("The average z-speed is:", np.mean(velocitiesz), "m/s")
    #If you repeat this enough times the average velocity should be 0, this is
    #the mean of the Gaussian distribution
    
    
    #c
    positions[:,0] = positions[:,0] + velocitiesx*deltat #Particles propagate
    positions[:,1] = positions[:,1] + velocitiesy*deltat
    positions[:,2] = positions[:,2] + velocitiesz*deltat
    
    
    #d
    pos = np.nonzero(positions > L) #Particles out of the box on the positive side
    neg = np.nonzero(positions < 0) #Particles out of the box on the negative side
    #momentum=momentum + m*(np.sqrt(velocitiesx[pos[:,1]]**2+velocitiesy[pos[:,1]]**2+velocitiesz[pos[:,1]]**2))
    #The momentum times the amount of times the particles hit the wall, so
    #you count all momenta. Then the sum over this is taken
    
    positions[pos] = L - (positions[pos]-L) #Place particle on the positive side
                                            #back in the box
    positions[neg] = 0 - (positions[neg]-0) #Place particle on the negative side
                                            #back in the box
    
    
    all_positions.append(positions.copy())


all_positions=np.array(all_positions)

#e
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(all_positions[:,0][:,0],all_positions[:,0][:,1],all_positions[:,0][:,2], marker='o')
ax.plot(all_positions[:,1][:,0],all_positions[:,1][:,1],all_positions[:,1][:,2], marker='o')
ax.set_xlim(0,L)
ax.set_ylim(0,L)
ax.set_zlim(0,L)
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')
ax.set_title('Trajectories for 2 particles in the box')
plt.show()






                                  
                                  
                                  
                                  