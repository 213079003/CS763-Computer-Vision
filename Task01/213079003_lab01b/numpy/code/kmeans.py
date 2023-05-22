# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 20:23:20 2022

@author: Srinidhi
"""

import os
import random
import numpy as np
import matplotlib.pyplot as plt
# * YOU ARE NOT ALLOWED TO IMPORT ANYTHING ELSE  *#

seed = 0
random.seed(seed)
os.environ['PYTHONHASHSEED'] = str(seed)
np.random.seed(seed)

# Here is a template for the KMeans clustering class
# The class has two functions "fit" and "predict" that you need to implement
# The fit function generates and stores  cluster centers for the
# given data
# The predict function assigns the input data to clusters
# (as learned by the fit function)
#  The input X should be a numpy array of of dimensions (n_data, n_features)
#  n_data is the dataset size
#  n_features is the feature dimension. For example for 3D datapoints,
#  n_features will be 3
#  Do not hard code n_features to any value - We will test your code on
# high dimension data


class KMeans(object):
    def __init__(self, n_clusters):
        super(KMeans, self).__init__()
        self.n_clusters = n_clusters
        self.centers = None

    def fit(self, X):
        
        self.X = X
        self.n_data , self.n_features = X.shape
        max_iterations = 1000
        tolerance = 0  # to check the convergence
        iteration = 0
        
        # Intialise self.centers
        #TODO#
        if self.centers is None:
            
            self.centers = np.random.normal(0,0.2, size = (self.n_clusters,self.n_features))
            
         #TODO#  

        
        while True:
            # Assign data points to clusters
            #TODO#
            
            distances = np.zeros((self.n_data,self.n_clusters))

            labels = np.zeros((self.n_data,1))
            
             # calculating the euclidean distance between the chosen centers and sample points
            for i in range(self.n_clusters):
                
                distances[:,i] = np.linalg.norm( X- self.centers[i], axis = 1)
              # choosing the minimum distance   
            labels = np.argmin(distances, axis=1)
            #TODO#
            
            # Update cluster centers
            #TODO#
            
             # saving the chosen centers in another variable so that new centers can be updated 
            old_centers = self.centers 
            for i in range(self.n_clusters):
                # finding the new means
                self.centers[i] = np.mean(X[labels == i],axis=0)
                
            #TODO#

            # Breaking condition
            #TODO#
            old_center_distances = np.linalg.norm(old_centers - self.centers)
            if old_center_distances < tolerance or iteration > max_iterations:
                break
            old_centers = self.centers.copy()
            iteration += 1
            
            #TODO#
                


    # Returns a numpy array of dimensions (n_data,)
    def predict(self,X):
        # Assign data points to clusters
        #distances = np.zeros((X.shape[0],self.n_clusters))
        distances = np.zeros((self.n_data,self.n_clusters))
        for i in range(self.n_clusters):
            distances[:,i] = np.linalg.norm(X-self.centers[i], axis = 1)
        labels = np.argmin(distances, axis=1)
        return labels


# Feel free to experiment with this


NUM_CLUSTERS = 3

# Create data such that it naturally forms clusters in 2D space 
# shape of this numpy array should be (n_data, n_features)
# here n_data is the dataset size (should be 600)
# here n_feautures is the dataset size (should be 2)


data1 = np.random.multivariate_normal([3,2],[[0.5, 0.1],[0.1, 0.5]] , 200)
data2 = np.random.multivariate_normal([1,5], [[0.4, 0.1],[0.1,0.5]], 200)
data3 = np.random.multivariate_normal([0,1], [[0.5,0],[0,0.5]], 200)
dataIn = np.concatenate((data1, data2, data3))

# show data
plt.figure()
plt.scatter(dataIn[:,0], dataIn[:,1], alpha = 0.3, marker = 'o')
plt.title('Input Data')
plt.savefig('../results/inputCluster.png')


kmm = KMeans(n_clusters = NUM_CLUSTERS)
kmm.fit(dataIn)
preds = kmm.predict(dataIn)
plt.figure()
colors = ['b', 'r', 'g', 'c', 'm', 'y', 'k', 'lime', 'turquoise', 'blueviolet', 'crimson', 'peru', 'maroon']
for ci in range(NUM_CLUSTERS):
    indices = preds == ci
    plt.scatter(dataIn[indices,0],dataIn[indices,1], alpha = 0.3, marker = 'o', color = colors[ci%len(colors)], label = 'Cluster {}'.format(ci))
    plt.legend()
    plt.title('Clustered Data')
    plt.savefig('../results/outputCluster.png')
plt.show()