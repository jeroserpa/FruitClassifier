# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 16:08:19 2022

@author: jeros

K-means implementation

"""


from Fruits import Fruit as F

from matplotlib import pyplot as plt 
from random import seed
import random
import numpy as np
from scipy.spatial import distance

class kmeans:

    def __init__(self,Fruits,k = 3,centroids = None):
        
        self.Fruits = Fruits
        self.k = k
        self.centroids = []
        self.Firsttime = True
        
        
        #Min and max for random centroids
        hu1_min = 5.5
        hu1_max = 12.5
        hu3_min = 9.5
        hu3_max = 20
        
        seed(2)        
        
        
        #get or create first centroids
        if centroids is not None:
            self.centroids = centroids 
        else:
            for k in range(k):
                self.centroids.append((random.uniform(hu1_min, hu1_max),random.uniform(hu3_min, hu3_max)))
        print('First centroids')
        print(self.centroids)
        
        
        
        #Loop  for iterate on the k-menas algorithm
        
        flag = True
        tolerance = 0.001 #distance tolerance for the centroids update (less than this and it will stop iterating)
        while flag is True:
            new_centroids = self.estimate()
            
            distanceA = distance.euclidean(self.centroids[0], new_centroids[0])
            distanceB = distance.euclidean(self.centroids[1], new_centroids[1])
            distanceC = distance.euclidean(self.centroids[2], new_centroids[2])
        
            
            if distanceA< tolerance and distanceB< tolerance and distanceC < tolerance:
                flag = False
            print('Distances')
            print(distanceA,distanceB,distanceC)
   
    
            self.centroids = new_centroids
        print('------------------')
        print(self.centroids)
        print('------------------')
    
    def estimate(self):
        
        
        A,B,C = [],[],[]
        All = []
        for fruit in self.Fruits:
            position = (fruit.hu[1],fruit.hu[3])
            d = []
            
            All.append(position) #Load list with all fruits positions
            
            for c in self.centroids:
                d.append(distance.euclidean(position, c)) #For each centroid we calculate the distance with the current fruit and load it to a list
            
            nearest = np.argmin(d) #We obtain the index of the nearest centroid
            
            # we assign the fruit to a group corresponding to the nearest centroid
            if nearest == 0: 
                fruit.guess = 'A'
                A.append(position)
        
            if nearest == 1: 
                fruit.guess = 'B'
                B.append(position)
            if nearest == 2: 
                fruit.guess = 'C'
                C.append(position)
        
        '''Plot First centroids and all together'''
        
        if self.Firsttime is True:
        
            plt.scatter((np.asarray(All)[:,0]),(np.asarray(All)[:,1]))
            plt.scatter((np.asarray(self.centroids)[:,0]),(np.asarray(self.centroids)[:,1]),color = 'r',marker = 'X')
            plt.show()
            self.Firsttime = False
            
            
        '''update centroids'''
       \
        hu1_meanA = np.sum(p[0] for p in A)/len(A)  
        
        hu1_meanB = np.sum(p[0] for p in B)/len(B)  
        
        hu1_meanC = np.sum(p[0] for p in C)/len(C)  
        
        hu3_meanA = np.sum(p[1] for p in A)/len(A)  
        
        hu3_meanB = np.sum(p[1] for p in B)/len(B)  
        
        hu3_meanC = np.sum(p[1] for p in C)/len(C)  
        
        # print(hu1_meanA,hu3_meanA)
        # print(hu1_meanB,hu3_meanB)
        # print(hu1_meanC,hu3_meanC)
        
        new_centroids = [(hu1_meanA,hu3_meanA),(hu1_meanB,hu3_meanB),(hu1_meanC,hu3_meanC)]
            
  
        plt.scatter((np.asarray(A)[:,0]),(np.asarray(A)[:,1]))
        plt.scatter((np.asarray(B)[:,0]),(np.asarray(B)[:,1]))
        plt.scatter((np.asarray(C)[:,0]),(np.asarray(C)[:,1]))
        plt.scatter((np.asarray(self.centroids)[:,0]),(np.asarray(self.centroids)[:,1]),color = 'k',marker = 'X')

        plt.show()
        
        plt.scatter((np.asarray(A)[:,0]),(np.asarray(A)[:,1]))
        plt.scatter((np.asarray(B)[:,0]),(np.asarray(B)[:,1]))
        plt.scatter((np.asarray(C)[:,0]),(np.asarray(C)[:,1]))
        plt.scatter((np.asarray(new_centroids)[:,0]),(np.asarray(new_centroids)[:,1]),color = 'k',marker = 'X')
        # plt.scatter((np.asarray(self.centroids)[:,0]),(np.asarray(self.centroids)[:,1]),color = 'r',marker = 'X')

        plt.show()
        
        
        
        return new_centroids
        
        