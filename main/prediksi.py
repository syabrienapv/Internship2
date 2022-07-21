from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse

import pandas as pd
import numpy as np
import scipy as sp
import operator
import os

matrix_path = os.getcwd() + '\\main\\datas\\resep_sparse_matrix.npz'
dataset_path = os.getcwd() + '\\main\\datas\\data.csv'

def read_sparse():
    sparse_matrix = sparse.load_npz(matrix_path)
    return sparse_matrix

def read_dataset():
    dataset = pd.read_csv(dataset_path)
    return dataset

def norm_matrix():
    return 

def item_similarity():
    item_similarity = cosine_similarity(read_sparse())
    item_sim_dataset = pd.DataFrame(item_similarity, index = matriks_norm.index, columns = matriks_norm.index)
    return item_sim_dataset

# def cosine_similarity():
#     sm = read_sparse()
#     item_similarity = cosine_similarity(sm)
#     user_similarity = cosine_similarity(sm.T)
#     return item_similarity


print(read_dataset())
