"""
Created 10/21/24

@author Owen Heuschele

A set of functions to reprocess new datasets for model training, testing, and cross-referencing
"""

import pandas as pd
import numpy as np

#all functions here accomplish the same task for different data formats. 
#the purpose here is to extract a dataframe from 3 different csv files

def test_to_df(filename : str):

    dtypes = {
        'ip': 'uint32',
        'app': 'uint16',
        'device': 'uint16',
        'os': 'uint32',
        'channel': 'uint32',
        'day': 'uint32',
        'hour': 'uint32',
        'minute': 'uint32',
        'second': 'uint32',
        'click_id': 'uint64',
    }

    dataset : pd.DataFrame = pd.read_csv(filename, dtype=dtypes)

    return dataset

def train_to_df(filename : str):

    dtypes = {
        'ip': 'uint32',
        'app': 'uint16',
        'device': 'uint16',
        'os': 'uint32',
        'channel': 'uint32',
        'is_attributed': 'uint8',
        'day': 'uint32',
        'hour': 'uint32',
        'minute': 'uint32',
        'second': 'uint32',
        
    }

    dataset : pd.DataFrame = pd.read_csv(filename, dtype=dtypes)

    return dataset

def ref_to_df(filename : str):

    dtypes = {
        'is_attributed' : 'uint8',
        'click_id' : 'uint64',
          
    }

    reference : pd.DataFrame = pd.read_csv('crossref.csv', dtype=dtypes)

    return reference