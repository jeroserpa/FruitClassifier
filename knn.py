# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 15:30:51 2022

@author: jeros\
    
    knn
"""
from Fruits import Fruit as F

from matplotlib import pyplot as plt 
from random import seed
import random
import numpy as np
from scipy.spatial import distance
from scipy import stats



class knn:
    def __init__(self,Fruits_b,Fruits_o,Fruits_l,k = 3,d = 5,plot = True, debug = False):
        
        self.Fruits_b = Fruits_b
        self.Fruits_o = Fruits_o
        self.Fruits_l = Fruits_l
        self.k = k
        self.d = d
        
        
        # group_b = []
        # group_o = []
        # group_l = []
        
        self.Groups = { 0 : 'b',
                  1 : 'o',
                  2 : 'l'
                  }
        
        
        
        self.group_b = np.zeros((len(self.Fruits_b),3))
        self.group_o = np.zeros((len(self.Fruits_o),3))
        self.group_l = np.zeros((len(self.Fruits_l),3))
        
        n=0
        for fruit in Fruits_b:
            
            self.group_b[n,0] = 0
            self.group_b[n,1] = fruit.hu[1]
            self.group_b[n,2] = fruit.hu[3]
            n+=1
        
        n=0    
        for fruit in Fruits_o:
            self.group_o[n,0] = 1
            self.group_o[n,1] = fruit.hu[1]
            self.group_o[n,2] = fruit.hu[3]
            n+=1
        n=0
        for fruit in Fruits_l:
            self.group_l[n,0] = 2
            self.group_l[n,1] = fruit.hu[1]
            self.group_l[n,2] = fruit.hu[3]
            n+=1
            
        #neighborhood = group_b + group_o + group_l
        # print(group_o[:,1])
        # print(np.asarray(group_b)[:,1])
        
        plt.scatter( self.group_b[:,1], self.group_b[:,2])
        plt.scatter( self.group_o[:,1], self.group_o[:,2])
        plt.scatter( self.group_l[:,1], self.group_l[:,2])
        
        self.neighborhood = np.concatenate((self.group_b,self.group_o,self.group_l))
        #print(neighborhood.shape)
        
        
        
    def classify(self,Fruits):
        
        B,L,O = [],[],[]
        
        for fruit in Fruits:
            position = (fruit.hu[1],fruit.hu[3])
            d = np.zeros(len(self.neighborhood))
            
            for n in range(len(self.neighborhood)):
                p = (self.neighborhood[n,1],self.neighborhood[n,2])
                d[n] = (distance.euclidean(position, p))
            
            min = d.argsort()[:self.k]
            
            votes = np.zeros(self.k)
            
            for v in range(self.k):
                votes[v] = self.neighborhood[min[v],0]
            modes = stats.mode(votes)
            
            #print(modes[0].astype(int)[0],self.Groups[modes[0].astype(int)[0]])
            
            fruit.guess = self.Groups[modes[0].astype(int)[0]]
            
            if fruit.guess == 'b': 
                B.append(position)
        
            if fruit.guess == 'l': 
                L.append(position)
                
            if fruit.guess == 'o': 
                O.append(position)
    
        plot  = True
        
        if plot is True:    
                        
            if len(B) > 0:
                
                plt.scatter((np.asarray(B)[:,0]),(np.asarray(B)[:,1]),label = 'b',alpha = 0.5 )
    
            if len(O) > 0:
                plt.scatter((np.asarray(O)[:,0]),(np.asarray(O)[:,1]),label = 'o',alpha = 0.5)
            
            if len(L) > 0:
                plt.scatter((np.asarray(L)[:,0]),(np.asarray(L)[:,1]),label = 'l',alpha = 0.5)
        
        plt.legend(loc = 'lower right')
        plt.show()  

        errors = []
        for fruit in Fruits:
            if fruit.label == 'b' and fruit.label != fruit.guess:
                errors.append((fruit.label,fruit.guess))
            if fruit.label == 'o' and fruit.label != fruit.guess:
                errors.append((fruit.label,fruit.guess))
            if fruit.label == 'l' and fruit.label != fruit.guess:
                errors.append((fruit.label,fruit.guess))
        
     
     
     
        print('-------------------------')
    
    
        error_p = (len(errors)/len(Fruits))*100
        print('Categorization error percentage:')
        print(error_p,'%')
        print(errors)
       
        
        
        
def main():
        
    print("main")
        
if __name__ == '__main__':
        main()    
        
        
        
        
        
        
        
        
        