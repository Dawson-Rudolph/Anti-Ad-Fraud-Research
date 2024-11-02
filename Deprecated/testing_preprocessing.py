"""
Created 10/8/24

@author Owen Heuschele

A script to process data before testing
"""

#not using some but may become necessary in future
import os, math, time
import numpy as np
import pandas as pd

#define datatypes for non-datetime data
dtypes = {
    'ip': 'uint32',
    'app': 'uint16',
    'device': 'uint16',
    'os': 'uint32',
    'channel': 'uint32',
    'click_id': 'uint64',
}

#read test file, sets datatypes, should parse dates in relevent columns correctly, convert to dataframe
#reads extracted 20% data stored in new_test.csv 
dataset = pd.read_csv('new_test.csv', dtype=dtypes, parse_dates=['click_time']) 

#converts to date_time objects
dataset['click_time'] = pd.to_datetime(dataset['click_time'])

#add columns for day, hour, minute, second
dataset['day'], dataset['hour'], dataset['minute'], dataset['second'] = [

    dataset['click_time'].dt.day.astype('uint8'),
    dataset['click_time'].dt.hour.astype('uint8'),
    dataset['click_time'].dt.minute.astype('uint8'),
    dataset['click_time'].dt.second.astype('uint8')

]

#removes click_time and attributed_time from the dataframe
#click_time is no longer necessary due to separation and creation of day, hour, minute, second
#attributed_time is not necessary due to conveying the same information mathematically as is_attributed
dataset = dataset.drop(columns=['click_time', 'attributed_time'])

