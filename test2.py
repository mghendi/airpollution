from PIL import Image
from numpy import *
import os

def pca(X):
  # Principal Component Analysis
  # input: X, matrix with training data as flattened arrays in rows
  # return: projection matrix (with important dimensions first),
  # variance and mean

  #get dimensions
  num_data,dim = X.shape

  #center data
  mean_X = X.mean(axis=0)
  for i in range(num_data):
      X[i] -= mean_X

  if dim>100:
      print('PCA - compact trick used')
      M = dot(X,X.T) #covariance matrix
      e,EV = linalg.eigh(M) #eigenvalues and eigenvectors
      tmp = dot(X.T,EV).T #this is the compact trick
      V = tmp[::-1] #reverse since last eigenvectors are the ones we want
      S = sqrt(e)[::-1] #reverse since eigenvalues are in increasing order
  else:
      print('PCA - SVD used')
      U,S,V = linalg.svd(X)
      V = V[:num_data] #only makes sense to return the first num_data

   #return the projection matrix, the variance and the mean
  return V,S,mean_X

def get_images():
  path = './dataset/'
  images = []
  count = 0
  for f in os.listdir(path):
    images.append(asarray(Image.open(path +'/'+f)))

  return images

pca(get_images()[0[]0])