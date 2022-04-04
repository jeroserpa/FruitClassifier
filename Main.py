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
import random


from knn import knn


class FruitClassifier():
    
    def __init__(self,path_b,path_o,path_l,path_bt,path_ot,path_lt):
        
        self.path_b = path_b
        self.path_o = path_o
        self.path_l = path_l

        self.path_bt = path_bt
        self.path_ot = path_ot
        self.path_lt = path_lt        
    
        self.fruits_b = []
        self.fruits_o = []
        self.fruits_l = []
        self.fruits = []

        self.fruits_bt = []
        self.fruits_ot = []
        self.fruits_lt = []
        self.fruits_t = []



        #self.fruits_test = []
   
    
    
    
        '''training'''
        
        '''create lists with paths to each image'''
        bananas_training = glob.glob(self.path_b)

        oranges_training = glob.glob(self.path_o)
    
        lemons_training = glob.glob(self.path_l)
    
    
        '''Init Fruits objects'''
        #fruits_b = []
        for path in bananas_training:
            self.fruits_b.append(F(path,'b'))
            
        # fruits_o = []
        for path in oranges_training:
           self.fruits_o.append(F(path,'o'))        
        
        # fruits_l = []
        for path in lemons_training:
           self.fruits_l.append(F(path,'l'))      
           
        self.fruits = self.fruits_b + self.fruits_o + self.fruits_l
        
        '''Testing'''
        
        '''create lists with paths to each image'''
        bananas_training_t = glob.glob(self.path_bt)

        oranges_training_t = glob.glob(self.path_ot)
    
        lemons_training_t = glob.glob(self.path_lt)
    
    
        '''Init Fruits objects'''
        #fruits_b = []
        for path in bananas_training_t:
            self.fruits_bt.append(F(path,'b'))
            
        # fruits_o = []
        for path in oranges_training_t:
           self.fruits_ot.append(F(path,'o'))        
        
        # fruits_l = []
        for path in lemons_training_t:
           self.fruits_lt.append(F(path,'l'))      
           
        self.fruits_t = self.fruits_bt + self.fruits_ot + self.fruits_lt
        random.shuffle(self.fruits_t) # mix fruits to make it mor "realistic"
        
    def learn_kmeans(self,plot = False):
        '''k-means'''
          
        #self.fruits = self.fruits_b + self.fruits_l + self.fruits_o
          
        self.km = kmeans(self.fruits, plot = plot, debug = True)
        
        return self.km 
        
        
    def sort_kmeans(self,km,plot = True):  
        

        
        random.shuffle(self.fruits_t) # mix fruits to make it mor "realistic"
           
        km.classify(self.fruits_t,plot = plot)
        
        
        
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
    
    def start_knn(self,k = 3,plot = True):
        
        
        
        Knn = knn(self.fruits_b,self.fruits_o,self.fruits_l,k = k,plot = plot)

        return Knn
    def classify_knn(self,knn):
         pass 
    
def main():    
    
    path_b ="C:\\Users\\jeros\\OneDrive\\Documentos\\FING\\IA 1\\fruits-360_dataset\\fruits-360\\Training\\Banana\\*"
    path_o ="C:\\Users\\jeros\\OneDrive\\Documentos\\FING\\IA 1\\fruits-360_dataset\\fruits-360\\Training\\Orange\\*"
    path_l ="C:\\Users\\jeros\\OneDrive\\Documentos\\FING\\IA 1\\fruits-360_dataset\\fruits-360\\Training\\Lemon\\*" 
   
    path_bt ="C:\\Users\\jeros\\OneDrive\\Documentos\\FING\\IA 1\\fruits-360_dataset\\fruits-360\\Test\\Banana\\*"
    path_ot ="C:\\Users\\jeros\\OneDrive\\Documentos\\FING\\IA 1\\fruits-360_dataset\\fruits-360\\Test\\Orange\\*"
    path_lt ="C:\\Users\\jeros\\OneDrive\\Documentos\\FING\\IA 1\\fruits-360_dataset\\fruits-360\\Test\\Lemon\\*" 
   
    fc = FruitClassifier(path_b, path_o, path_l,path_bt,path_ot,path_lt) 
    
   
    #for i in range(7):
        #fc.histogram(i)
    
    # km = fc.learn_kmeans(plot = True)
    
    # fc.sort_kmeans(km,plot = True)
    

    # for i in range(2,10):
    #     #print(i)
    Knn = fc.start_knn(k =100,plot = True)

    Knn.classify(fc.fruits_t)

# 

if __name__ == '__main__':
    main()