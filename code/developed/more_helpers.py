import os
import numpy as np
import glob
import time
import csv
from sklearn.cluster import MiniBatchKMeans
from sklearn.cluster import SpectralClustering
import pandas as pd
        
        
def createCodebookSpectral(features, codebook_size=100):
    """Creates a visual BOW codebook"""
    train_features_to_encode = []
    for image_features in features:
        train_features_to_encode.append(image_features.data)
    train_features_to_encode = np.concatenate(train_features_to_encode, axis=0)
    #codebook = MiniBatchKMeans(n_clusters=codebook_size, batch_size=codebook_size * 10)
    codebook = SpectralClustering(n_clusters=codebook_size,eigen_solver='arpack', affinity='nearest_neighbors', n_jobs=-1)
    start = time.time()
    codebook.fit(train_features_to_encode)
    end = time.time()
    print('training took {} seconds'.format(end-start))
    return codebook
