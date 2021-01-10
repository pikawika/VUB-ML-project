import os
import numpy as np
import glob
import time
import csv
from sklearn.preprocessing import PowerTransformer
from sklearn.cluster import MiniBatchKMeans
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
import pandas as pd

# default
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

# higer max iterations, lower number of inits to reduce computational time
def createCodebookFullK(features, codebook_size=100):
    """Creates a visual BOW codebook"""
    print("Using n_init = 4 and max_iter = 500")
    train_features_to_encode = []
    for image_features in features:
        train_features_to_encode.append(image_features.data)
    train_features_to_encode = np.concatenate(train_features_to_encode, axis=0)
    codebook = KMeans(n_clusters=codebook_size,
                      n_init = 4,
                      max_iter = 500,
                      n_jobs = -1,
                      verbose = 3)
    start = time.time()
    codebook.fit(train_features_to_encode)
    end = time.time()
    print('training took {} seconds'.format(end-start))
    return codebook

# higer max iterations, lower number of inits to reduce computational time, transforms data
def createCodebookFullKWithPreProc(features, codebook_size=100):
    """Creates a visual BOW codebook"""
    print("Using n_init = 4 and max_iter = 500")
    print("Using PowerTransformer")
    train_features_to_encode = []
    for image_features in features:
        train_features_to_encode.append(image_features.data)
    train_features_to_encode = np.concatenate(train_features_to_encode, axis=0)
    scaler = PowerTransformer()
    codebook = KMeans(n_clusters=codebook_size,
                      n_init = 4,
                      max_iter = 500,
                      n_jobs = -1,
                      verbose = 3)
    start = time.time()
    train_features_to_encode = scaler.fit_transform(train_features_to_encode)
    codebook.fit(train_features_to_encode)
    end = time.time()
    print('training took {} seconds'.format(end-start))
    return codebook

# Transforms data using PowerTransformer, which was optimal
def createCodebookMiniKWithPreProc(features, codebook_size=100):
    """Creates a visual BOW codebook"""
    print("Using PowerTransformer")
    train_features_to_encode = []
    for image_features in features:
        train_features_to_encode.append(image_features.data)
    train_features_to_encode = np.concatenate(train_features_to_encode, axis=0)
    scaler = PowerTransformer()
    codebook = MiniBatchKMeans(n_clusters=codebook_size,
                               max_iter = 100,
                               reassignment_ratio = 0.01,
                               batch_size=codebook_size * 30)
    start = time.time()
    train_features_to_encode = scaler.fit_transform(train_features_to_encode)
    #train_features_to_encode = np.multiply(train_features_to_encode, np.abs(train_features_to_encode))
    codebook.fit(train_features_to_encode)
    end = time.time()
    print('training took {} seconds'.format(end-start))
    return codebook, scaler

# when encoding images, the data of the image should also be transformed with the same scaler/transformer used for clustering
def encodeImageWithPreProc(features, codebook, scaler):
    """Encodes one image given a visual BOW codebook"""
    # find the minimal feature distance for all patches of the image
    features = scaler.transform(features)
    #features = np.multiply(features, np.abs(features))
    visual_words = codebook.predict(features)
    word_occurrence = pd.DataFrame(visual_words, columns=['cnt'])['cnt'].value_counts() 
    bovw_vector = np.zeros(codebook.n_clusters) 
    for key in word_occurrence.keys():
        bovw_vector[key] = word_occurrence[key]
    bovw_feature = bovw_vector / np.linalg.norm(bovw_vector)
    return bovw_feature

# to optimize
def createCodebookGaussianMixture(features, codebook_size=100):
    """Creates a visual BOW codebook"""
    train_features_to_encode = []
    for image_features in features:
        train_features_to_encode.append(image_features.data)
    train_features_to_encode = np.concatenate(train_features_to_encode, axis=0)
    codebook = GaussianMixture(n_components=codebook_size,
                               max_iter = 200,
                               n_init = 4,
                               verbose = 3,
                               verbose_interval = 25
                              )
    start = time.time()
    codebook.fit(train_features_to_encode)
    end = time.time()
    print('training took {} seconds'.format(end-start))
    return codebook