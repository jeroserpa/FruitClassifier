# -*- coding: utf-8 -*-
"""
Fruit Class
"""
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

class Fruit:
    def __init__(self,path,label=None, debug = False):
        self.path = path
        self.label = label
        self.guess = None
        self.hu = np.zeros(7)        
        
        self.debug = debug
      
        self.calc_features()
   
    def calc_features(self):
        
        img = cv.cvtColor(cv.imread(self.path),cv.COLOR_BGR2RGB) 
        img_g = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img_gf = np.zeros((100,100,1),np.uint8)
        
        if self.debug is True:
            plt.figure(1)
            plt.imshow(img)
            # plt.figure(2)
            #plt.imshow(img_g,cmap='gray') 
        
        img_gf = cv.bilateralFilter(img_g,15,80,80)
        
        if self.debug is True:
            plt.imshow(img_gf,cmap='gray') 
        
        
        '''Threshold image'''
        _,img_b = cv.threshold(img_gf, 200, 255, cv.THRESH_BINARY)
        img_b = np.invert(img_b)
        
        
        if self.debug is True:

            '''Show binarization'''
            plt.figure(3)
            plt.imshow(img_b,cmap='gray') 
        
        
        
        '''Calculate Moments''' 
        moments = cv.moments(img_b) 
        '''Calculate Hu Moments''' 
        huMoments = cv.HuMoments(moments)
        #print(huMoments)
        '''Log scale hu moments''' 
        hu = -np.sign(huMoments) * np.log10(np.abs(huMoments))

        for i in range(7):
            self.hu[i] = hu[i,0] 

        if self.debug is True:
            print('Hu moments')
            print(self.hu)      
        
        
        
        
        
def main():
    
    #path = r'C:\\Users\\jeros\\OneDrive\\Documentos\\FING\\IA 1\\fruits-360_dataset\\fruits-360\\Training\\Banana\\0_100.jpg'
    path = r'C:\\Users\\jeros\\OneDrive\\Documentos\\FING\\IA 1\\fruits-360_dataset\\fruits-360\\Training\\Orange\\0_100.jpg'
    
    F = Fruit(path,debug = False)
    
if __name__ == '__main__':
    main()