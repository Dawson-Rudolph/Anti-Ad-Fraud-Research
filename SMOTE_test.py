"""
Created 9/30/24

@author Owen Heuschele

A script to balance a dataset of clicks using SMOTE
"""

import os, math, time
import numpy as np
import pandas as pd
import sklearn
import imblearn

dtypes = {
    'ip': 'uint32',
    'app': 'object',
    'device': 'object',
    'os': 'object',
    'channel': 'object',
    'is_attributed': 'uint8',
}
dataset = pd.read_csv('test.csv', dtype=dtypes, parse_dates=['click_time'])   

dataset['click_time'] = pd.to_datetime(dataset['click_time'])

dataset['year'], dataset['month'], dataset['day'], dataset['hour'], dataset['minute'], dataset['second'] = [

    dataset['click_time'].dt.year.astype('uint8'),
    dataset['click_time'].dt.month.astype('uint8'),
    dataset['click_time'].dt.day.astype('uint8'),
    dataset['click_time'].dt.hour.astype('uint8'),
    dataset['click_time'].dt.minute.astype('uint8'),
    dataset['click_time'].dt.second.astype('uint8')

]