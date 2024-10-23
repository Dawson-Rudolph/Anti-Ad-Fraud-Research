"""
Created 10/21/24

@author Owen Heuschele

A script to add additional processing to a testing dataframe
"""
import pandas as pd
import numpy as np

def additional_test_process(test_df : pd.DataFrame):

    #add click id feature for test accuracy scoring
    test_df['click_id'] = range(1, len(test_df)+1)

    #add new dataframe with binary yes/no fraud class and click id class for said accuracy scoring
    crossref_df : pd.DataFrame = pd.DataFrame({'is_attributed': test_df['is_attributed'], 'click_id' : test_df['click_id']})

    #remove is attributed from test set so as not to impact the model
    test_df.drop(columns=['is_attributed'], inplace=True)

    return test_df, crossref_df