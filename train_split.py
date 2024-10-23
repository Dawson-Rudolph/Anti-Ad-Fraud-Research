"""
Created 10/21/24

@author Owen Heuschele

A script to split training data into a training set and a testing set
"""


import pandas as pd
import numpy as np
import training_preprocess as initial_pp
import test_preprocess_new as test_pp
from sklearn.model_selection import train_test_split


def train_test_ref_split(filename : str):
    
    #run initial preprocessing on training set and collect a dataframe
    dataset_raw = initial_pp.pre_process_train(filename)

    #split dataset 80:20 for testing purposes
    split = train_test_split(dataset_raw, test_size=0.2, random_state=23)

    #defined so as opposed to unpacking to better define variable types
    train_df : pd.DataFrame = split[0]
    test_df : pd.DataFrame = split[1]

    #unpack additional processing (adding click id, moving classifier variable class to a reference dataset)
    test_df, crossref_df = test_pp.additional_test_process(test_df)

    return train_df, test_df, crossref_df


if __name__ == '__main__':

    #run above code
    train_df, test_df, crossref_df = train_test_ref_split('train.csv')

    #parse to new csv files
    train_df.to_csv('new_train.csv', index=False)
    test_df.to_csv('new_test.csv', index=False)
    crossref_df.to_csv('crossref.csv', index=False)