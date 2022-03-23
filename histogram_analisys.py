# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 15:37:26 2022

@author: jeros

Hu moments analysis
"""
import numpy as np
from matplotlib import pyplot as plt 
from matplotlib.ticker import PercentFormatter


def plotter(huN = 1, bananas = None,oranges = None,lemons = None):
    


   # if bananas is not None:
   #     plt.hist(bananas[0,:],bins, alpha=0.5, label='b',weights = weights_b )
   # if oranges is not None:
   #     plt.hist(oranges[0,:],bins, alpha=0.5, label='o',weights = weights_o)
  

   '''Hu moment number histogram'''
   if huN == 0:
       bins = np.linspace(2.85,3.22,100)
       
   if huN == 1:
       bins = np.linspace(5.5,12.5,100)
   
   if huN == 2:
       bins = np.linspace(10,16,100)
 
   if huN == 3:
       bins = np.linspace(9.8,19,100)
 
   if huN == 4:
       bins = np.linspace(-35,35,100)

   if huN == 5:
        bins = np.linspace(-25,25,100)
  
   if huN == 6:
        bins = np.linspace(-35,35,100)   
  
    
   #plt.hist([bananas[huN,:], oranges[huN,:],lemons[huN,:]],label=['B', 'O','L'])
   plt.hist([bananas[huN,:], oranges[huN,:],lemons[huN,:]], bins,label=['B', 'O','L'],density = True)
   
   plt.title('Hu'+str(huN))
      
 

   '''Hu moment number 2 histogram'''
   bins = np.linspace(10,16,100)
    

   
   
   
  
   
    
   
    
   
   plt.legend(loc='upper right')
   plt.autoscale(enable=True, axis='x', tight=True)
   #plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
   plt.show()