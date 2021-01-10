import os
import numpy as np
import glob
import time
import csv
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import MiniBatchKMeans
from sklearn.cluster import KMeans
from sklearn.cluster import GaussianMixture
import pandas as pd

# to optimize
def createCodebookAffinity(features, codebook_size=100):
    """Creates a visual BOW codebook"""
    train_features_to_encode = []
    for image_features in features:
        train_features_to_encode.append(image_features.data)
    train_features_to_encode = np.concatenate(train_features_to_encode, axis=0)
    #codebook = MiniBatchKMeans(n_clusters=codebook_size, batch_size=codebook_size * 10)
    codebook = AffinityPropagation()
    start = time.time()
    codebook.fit(train_features_to_encode)
    end = time.time()
    print('training took {} seconds'.format(end-start))
    return codebook

# to optimize
def createCodebookMiniK(features, codebook_size=100):
    """Creates a visual BOW codebook"""
    train_features_to_encode = []
    for image_features in features:
        train_features_to_encode.append(image_features.data)
    train_features_to_encode = np.concatenate(train_features_to_encode, axis=0)
    codebook = MiniBatchKMeans(n_clusters=codebook_size,
                               max_iter = 100,
                               reassignment_ratio = 0.01,
                               batch_size=codebook_size * 30)
    start = time.time()
    codebook.fit(train_features_to_encode)
    end = time.time()
    print('training took {} seconds'.format(end-start))
    return codebook

# to optimize (crtly testing)
def createCodebookFullK(features, codebook_size=100):
    """Creates a visual BOW codebook"""
    print("Using n_init = 10 and max_iter = 600")
    train_features_to_encode = []
    for image_features in features:
        train_features_to_encode.append(image_features.data)
    train_features_to_encode = np.concatenate(train_features_to_encode, axis=0)
    codebook = KMeans(n_clusters=codebook_size,
                      n_init = 10,
                      max_iter = 600,
                      n_jobs = -1,
                      verbose = 3)
    start = time.time()
    codebook.fit(train_features_to_encode)
    end = time.time()
    print('training took {} seconds'.format(end-start))
    return codebook

# to optimize
def createCodebookMiniKWithPreProc(features, codebook_size=100):
    """Creates a visual BOW codebook"""
    train_features_to_encode = []
    for image_features in features:
        train_features_to_encode.append(image_features.data)
    train_features_to_encode = np.concatenate(train_features_to_encode, axis=0)
    scaler = StandardScaler()
    codebook = MiniBatchKMeans(n_clusters=codebook_size,
                               max_iter = 100,
                               reassignment_ratio = 0.01,
                               batch_size=codebook_size * 30)
    start = time.time()
    train_features_to_encode = scaler.fit_transform(train_features_to_encode)
    codebook.fit(train_features_to_encode)
    end = time.time()
    print('training took {} seconds'.format(end-start))
    return codebook

# to optimize
def createCodebookMiniK(features, codebook_size=100):
    """Creates a visual BOW codebook"""
    train_features_to_encode = []
    for image_features in features:
        train_features_to_encode.append(image_features.data)
    train_features_to_encode = np.concatenate(train_features_to_encode, axis=0)
    codebook = GaussianMixture(n_components=codebook_size,
                               max_iter = 100,
                               n_init = 1)
    start = time.time()
    codebook.fit(train_features_to_encode)
    end = time.time()
    print('training took {} seconds'.format(end-start))
    return codebook