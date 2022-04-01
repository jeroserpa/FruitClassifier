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

    def __init__(self,Fruits,k = 3,centroids = None,plot = True, debug = False):
        
        self.Fruits = Fruits # list of Fruit objects
        self.k = k # K for kmeans, FIXED AT 3 (it was supposed to be variable but fixed for convinience )
        self.centroids = [] #centroid at each iteration 
        self.learned_centroids = [] #final centroids after iterating
        self.Firsttime = True 
        self.plot = plot #flag to plot
        self.debug = debug #flag to print info
        self.iterations = 0 #number of iteration until tolerance reached 
        self.tolerance = 0.1 #distance tolerance for the centroids update (less than this and it will stop iterating)
        
        self.category = [None] * 3 #used to find groups labels 
        
        #voting system to find groups labels
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
        
        self.Groups = { }
        
        
        
        #Min and max for random centroids
        hu1_min = 5.5
        hu1_max = 12.5
        hu3_min = 9.5
        hu3_max = 20
        
        seed(1)
        #seed(2)        
        
        
        #get or create first centroids
        if centroids is not None:
            self.centroids = centroids 
        else:
            for k in range(k):
                self.centroids.append((random.uniform(hu1_min, hu1_max),random.uniform(hu3_min, hu3_max)))
        
        if self.debug is True:
            print('First centroids:')
            print(self.centroids)
        
        
        
        #Loop  for iterate on the k-menas algorithm
        
        flag = True
        while flag is True:
            new_centroids = self.estimate()
            
            distanceA = distance.euclidean(self.centroids[0], new_centroids[0])
            distanceB = distance.euclidean(self.centroids[1], new_centroids[1])
            distanceC = distance.euclidean(self.centroids[2], new_centroids[2])
        
            
            if distanceA< self.tolerance and distanceB< self.tolerance and distanceC < self.tolerance:
                flag = False
            
            if self.debug is True:
                print('Distances:')
                print(distanceA,distanceB,distanceC)
   
    
            self.centroids = new_centroids
            self.iterations += 1
        
        
        self.learned_centroids = self.centroids
        print('------------------')
        print('Learned centroids:')
        print(self.learned_centroids)
        print('------------------')
        
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
        
        self.Groups = {
            'A': self.category[0],
            'B': self.category[1],
            'C': self.category[2]
            }
        
        #print(Groups)
        
        
        
        '''Find wrong categorization'''
        
        notB = []
        notO = []
        notL = []
        errors = []
        for fruit in Fruits:
            if fruit.label == 'b' and fruit.label != self.Groups[fruit.guess]:
                notB.append(fruit)
                errors.append((fruit.label,self.Groups[fruit.guess]))
            if fruit.label == 'o' and fruit.label != self.Groups[fruit.guess]:
                notO.append(fruit)
                errors.append((fruit.label,self.Groups[fruit.guess]))
            if fruit.label == 'l' and fruit.label != self.Groups[fruit.guess]:
                notL.append(fruit)
                errors.append((fruit.label,self.Groups[fruit.guess]))
       
        if debug is True:
            print('Errors(label,guess):')
            print(errors)
            print(len(errors))
            print('Number of fruits analyzed:')
            print(len(Fruits))
        
        
        
        
        error_p = (len(errors)/len(Fruits))*100
        print('Categorization error percentage:')
        print(error_p,'%')
        
        print('Tolerance:')
        print(self.tolerance)
        print('Number of iterations:')
        print(self.iterations)
        
        # print(len(notO),len(notL))
        # for fruit in notL:
        #     print(fruit.label)
        
        
        
        
        
    
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
                if fruit.label == "b":
                    self.Av['b']+=1
                elif fruit.label == "o":
                    self.Av['o']+=1
                elif fruit.label == "l":
                    self.Av['l']+=1
        
            if nearest == 1: 
                fruit.guess = 'B'
                B.append(position)
                '''vote for centroid label'''
                if fruit.label == "b":
                    self.Bv['b']+=1
                elif fruit.label == "o":
                    self.Bv['o']+=1
                elif fruit.label == "l":
                    self.Bv['l']+=1
                
                
            if nearest == 2: 
                fruit.guess = 'C'
                C.append(position)
                '''vote for centroid label'''
                if fruit.label == "b":
                    self.Cv['b']+=1
                elif fruit.label == "o":
                    self.Cv['o']+=1
                elif fruit.label == "l":
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
        
            
        
        
        
        
        
        
        
        
        
        
        