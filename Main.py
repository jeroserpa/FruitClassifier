# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 15:06:53 2022

@author: jeros

Main
"""


import glob
from Fruits import Fruit as F
import numpy as np
from histogram_analisys import plotter
from k_means import kmeans 



def main():
    
   # print(glob.glob("C:\\Users\\jeros\\OneDrive\\Documentos\\FING\\IA 1\\fruits-360_dataset\\fruits-360\\Training\\Banana\\*"))
    
    bananas_training = glob.glob("C:\\Users\\jeros\\OneDrive\\Documentos\\FING\\IA 1\\fruits-360_dataset\\fruits-360\\Training\\Banana\\*")

    oranges_training = glob.glob("C:\\Users\\jeros\\OneDrive\\Documentos\\FING\\IA 1\\fruits-360_dataset\\fruits-360\\Training\\Orange\\*")

    lemons_training = glob.glob("C:\\Users\\jeros\\OneDrive\\Documentos\\FING\\IA 1\\fruits-360_dataset\\fruits-360\\Training\\Lemon\\*")

    
    '''Init Fruits objects'''
    fruits_b = []
    for path in bananas_training:
        fruits_b.append(F(path,'bananas'))
        
    fruits_o = []
    for path in oranges_training:
       fruits_o.append(F(path,'oranges'))        

    fruits_l = []
    for path in lemons_training:
       fruits_l.append(F(path,'lemons'))            
        
    
    mean0 = np.mean([f.hu[0] for f in fruits_l])
    # sd0 = np.std([f.hu[0] for f in fruits])
    
    #print(mean0)
    # print(sd0)

    #print(fruits[0].hu.shape)
  
    
  
    '''Retreive Hu moments'''

    hu_b = np.zeros((7,len(fruits_b)),dtype=np.float_) 
    
    for f in range(0,len(fruits_b)):
           hu_b[:,f] = fruits_b[f].hu[:]
    #print(hu_b)
    
    hu_o = np.zeros((7,len(fruits_o)),dtype=np.float_) 
        
    for f in range(0,len(fruits_o)):
           hu_o[:,f] = fruits_o[f].hu[:]
    #print(hu_o)
    
    hu_l = np.zeros((7,len(fruits_l)),dtype=np.float_) 
    
    for f in range(0,len(fruits_l)):
           hu_l[:,f] = fruits_l[f].hu[:]
    #print(hu_o)
    
    
    #plotter(0,hu_b,hu_o,hu_l)
    
    
    '''k-means'''
    
    fruits = fruits_b + fruits_l + fruits_o
    
    km = kmeans(fruits)
    
    
    
    
    
    
    
    
    
    
    

if __name__ == '__main__':
    main()