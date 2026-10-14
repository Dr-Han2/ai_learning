"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
import numpy as np
from collections import defaultdict
from scipy.special import digamma, gamma
from sklearn.utils.multiclass import unique_labels
import random

#________1. DAG 生成   ________
def generate_dag(n, p=0.5, seed=None):
    rng = np.random.default_rng(seed)