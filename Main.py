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



class FruitClassifier():
    
    def __init__(self,path_b,path_o,path_l):
        
        self.path_b = path_b
        self.path_o = path_o
        self.path_l = path_l
  
    
        self.fruits_b = []
        self.fruits_o = []
        self.fruits_l = []
        self.fruits = []
        #self.fruits_test = []
   
    
    
    
   
        
        '''create lists with paths to each image'''
        bananas_training = glob.glob(self.path_b)

        oranges_training = glob.glob(self.path_o)
    
        lemons_training = glob.glob(self.path_l)
    
    
        '''Init Fruits objects'''
        #fruits_b = []
        for path in bananas_training:
            self.fruits_b.append(F(path,'bananas'))
            
        # fruits_o = []
        for path in oranges_training:
           self.fruits_o.append(F(path,'oranges'))        
        
        # fruits_l = []
        for path in lemons_training:
           self.fruits_l.append(F(path,'lemons'))            
     
        
    def learn(self,plot = False):
        '''k-means'''
          
        self.fruits = self.fruits_b + self.fruits_l + self.fruits_o
          
        self.km = kmeans(self.fruits, plot = plot)
        
        return self.km 
        
        
    def sort(self,km,path_t,plot = True):  
        
        fruits_test = []
        
        fruits_test_paths = glob.glob(path_t)
        for path in fruits_test_paths:
            fruits_test.append(F(path,'bananas'))
            
        km.classify(fruits_test,plot = plot)
        
        
        
        '''
        #mean0 = np.mean([f.hu[0] for f in fruits_l])
        # sd0 = np.std([f.hu[0] for f in fruits])
        
        #print(mean0)
        # print(sd0)
    
        #print(fruits[0].hu.shape)
        '''

  
    def histogram(self,hu_moment_N = 1):  
        '''This function lets you analyze the distribution of image features in a Histogram'''
        
        
        '''Retreive Hu moments'''
        
        hu_b = np.zeros((7,len(self.fruits_b)),dtype=np.float_) 
        
        for f in range(0,len(self.fruits_b)):
               hu_b[:,f] = self.fruits_b[f].hu[:]
        #print(hu_b)
        
        hu_o = np.zeros((7,len(self.fruits_o)),dtype=np.float_) 
            
        for f in range(0,len(self.fruits_o)):
               hu_o[:,f] = self.fruits_o[f].hu[:]
        #print(hu_o)
        
        hu_l = np.zeros((7,len(self.fruits_l)),dtype=np.float_) 
        
        for f in range(0,len(self.fruits_l)):
               hu_l[:,f] = self.fruits_l[f].hu[:]
               #print(hu_o)
    
    
        plotter(hu_moment_N,hu_b,hu_o,hu_l)
    
    

    
    
def main():    
    
    path_b ="C:\\Users\\jeros\\OneDrive\\Documentos\\FING\\IA 1\\fruits-360_dataset\\fruits-360\\Training\\Banana\\*"
    path_o ="C:\\Users\\jeros\\OneDrive\\Documentos\\FING\\IA 1\\fruits-360_dataset\\fruits-360\\Training\\Orange\\*"
    path_l ="C:\\Users\\jeros\\OneDrive\\Documentos\\FING\\IA 1\\fruits-360_dataset\\fruits-360\\Training\\Lemon\\*" 
    
    #path_t = "C:\\Users\\jeros\\OneDrive\\Documentos\\FING\IA 1\\fruits-360_dataset\\fruits-360\\Test\\Banana\\*"
    path_t = "C:\\Users\\jeros\\OneDrive\\Documentos\\FING\\IA 1\\fruits-360_dataset\\fruits-360\\Test\\Bananas+Oranges+Lemons\\*"
    fc = FruitClassifier(path_b, path_o, path_l) 
    
    #fc.histogram()
    km = fc.learn(plot = False)
    
    fc.sort(km,path_t,plot = True)
    

if __name__ == '__main__':
    main()