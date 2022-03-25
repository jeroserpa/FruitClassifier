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

    def __init__(self,Fruits,k = 3,centroids = None,plot = True):
        
        self.Fruits = Fruits
        self.k = k
        self.centroids = []
        self.learned_centroids = []
        self.Firsttime = True
        self.plot = plot
        
        self.category = [None] * 3
        
        self.Av = {
            'b': 0,
            'o': 0,
            'l': 0
            }
        self.Bv = {
            'b': 0,
            'o': 0,
            'l': 0
            }
        self.Cv = {
            'b': 0,
            'o': 0,
            'l': 0
            }
        
        
        
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
        
        
        
        self.learned_centroids = self.centroids
        print('------------------')
        print(self.learned_centroids)
        print('------------------')
        
        
    
    def estimate(self):
        self.Av = {
            'b': 0,
            'o': 0,
            'l': 0
            }
        self.Bv = {
            'b': 0,
            'o': 0,
            'l': 0
            }
        self.Cv = {
            'b': 0,
            'o': 0,
            'l': 0
            }
        
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
                '''vote for centroid label'''
                if fruit.label == "bananas":
                    self.Av['b']+=1
                elif fruit.label == "oranges":
                    self.Av['o']+=1
                elif fruit.label == "lemons":
                    self.Av['l']+=1
        
            if nearest == 1: 
                fruit.guess = 'B'
                B.append(position)
                '''vote for centroid label'''
                if fruit.label == "bananas":
                    self.Bv['b']+=1
                elif fruit.label == "oranges":
                    self.Bv['o']+=1
                elif fruit.label == "lemons":
                    self.Bv['l']+=1
                
                
            if nearest == 2: 
                fruit.guess = 'C'
                C.append(position)
                '''vote for centroid label'''
                if fruit.label == "bananas":
                    self.Cv['b']+=1
                elif fruit.label == "oranges":
                    self.Cv['o']+=1
                elif fruit.label == "lemons":
                    self.Cv['l']+=1
    
        #Debug for voting system
        # print('Votes')
        # print(self.Av,self.Bv,self.Cv)
        # print(max(self.Av, key=self.Av.get))    
        # print(len(self.Fruits))
        
        '''Plot First centroids and all together'''
        
        if self.Firsttime is True:
            if self.plot is True:
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
            
        if self.plot is True:
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
        
    
    def classify(self,Fruits,plot = True):
        
        A,B,C = [],[],[] 
        
        '''This blocks finds the correct label for each category'''
        
        
        
        if max(self.Av, key=self.Av.get) == 'b':
            self.category[0] = 'b'
        elif max(self.Av, key=self.Av.get) == 'o':    
            self.category[0] = 'o'
        elif max(self.Av, key=self.Av.get) == 'l':    
            self.category[0] = 'l'
        
        if max(self.Bv, key=self.Bv.get) == 'b':
            self.category[1] = 'b'
        elif max(self.Bv, key=self.Bv.get) == 'o':    
            self.category[1] = 'o'
        elif max(self.Bv, key=self.Bv.get) == 'l':    
            self.category[1] = 'l'    
            
        if max(self.Cv, key=self.Cv.get) == 'b':
            self.category[2] = 'b'
        elif max(self.Cv, key=self.Cv.get) == 'o':    
            self.category[2] = 'o'
        elif max(self.Cv, key=self.Cv.get) == 'l':    
            self.category[2] = 'l'     
        
        '''   '''  
            
        '''we analyze each fruit and put it in the estimated category'''
        for fruit in Fruits:
            position = (fruit.hu[1],fruit.hu[3])
            d = []
                        
            for c in self.learned_centroids:
                d.append(distance.euclidean(position, c)) #For each centroid we calculate the distance with the current fruit and load it to a list
            
            nearest = np.argmin(d) #We obtain the index of the nearest centroid
            
            # we assign the fruit to a group corresponding to the nearest centroid
            if nearest == 0: 
                fruit.guess = self.category[nearest]
                A.append(position)
        
            if nearest == 1: 
                fruit.guess = self.category[nearest]
                B.append(position)
            if nearest == 2: 
                fruit.guess = self.category[nearest]
                C.append(position)
                
            #print(fruit.guess)
            #print(fruit.label)
                
        if plot is True:    
                        
            if len(A) > 0:
                
                plt.scatter((np.asarray(A)[:,0]),(np.asarray(A)[:,1]),label = self.category[0] )
    
            if len(B) > 0:
                plt.scatter((np.asarray(B)[:,0]),(np.asarray(B)[:,1]),label = self.category[1])
            
            if len(C) > 0:
                plt.scatter((np.asarray(C)[:,0]),(np.asarray(C)[:,1]),label = self.category[2])
    
            plt.scatter((np.asarray(self.learned_centroids)[:,0]),(np.asarray(self.learned_centroids)[:,1]),color = 'k',marker = 'X')
    
        
            plt.legend(loc = 'lower right')
            plt.show()  
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        