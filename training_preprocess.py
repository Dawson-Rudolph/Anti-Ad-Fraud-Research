"""
Created 10/4/24

@author Owen Heuschele

A script to process data before training
"""

#not using some but may become necessary in future
import os, math, time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#define datatypes for non-datetime data
dtypes = {
    'ip': 'uint32',
    'app': 'uint16',
    'device': 'uint16',
    'os': 'uint32',
    'channel': 'uint32',
    'is_attributed': 'uint8',
}

#read train file, sets datatypes, should parse dates in relevent columns correctly, convert to dataframe
#here I'm using sample to save space, actual training set is 'new_train.csv'
dataset = pd.read_csv('train_sample.csv', dtype=dtypes, parse_dates=['click_time']) 

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


#below is simply code to make a pie chart and a line to make a corr matrix that I haven't had
#time to mess around with yet.
#commented out for ease of use of above code
"""
corrM = dataset.corr()
#print(corrM)

pieData = dataset['is_attributed'].value_counts()

#collect value counts
osData = dataset['os'].value_counts()
appData = dataset['app'].value_counts()
deviceData = dataset['device'].value_counts()

#extract value counts
keyValLists = []
for i in (osData, appData, deviceData):
    keyValLists.append(list(zip(i.keys().to_list(), i.to_list())))

osData, appData, deviceData = keyValLists
osInf, appInf, deviceInf = [], [], []
osF, appF, deviceF = [], [], []

#seperate infrequent values
for i in osData:
    if i[1] < 600:
        osInf.append(i[1])
    else:
        osF.append(i)

for i in appData:
    if i[1] < 600:
        appInf.append(i[1])
    else:
        appF.append(i)

for i in deviceData:
    if i[1] < 600:
        deviceInf.append(i[1])
    else:
        deviceF.append(i)

#combine infrequent and frequent values
osData = osF + [('other', sum(osInf))]
appData = appF + [('other', sum(appInf))]
deviceData = deviceF + [('other', sum(deviceInf))]

#convert to data frame
osData = pd.DataFrame(osData, columns=['os version id', 'counts'])
appData = pd.DataFrame(appData, columns=['app id', 'counts'])
deviceData = pd.DataFrame(deviceData, columns=['device id', 'counts'])
    
#plot on horizontal bar graph, manually one at a time as no need to do that often
#deviceData.plot.barh(y='counts', x='device id', color='#9a6bd1')
#osData.plot.barh(y='counts', x='os version id', color='#9a6bd1')
appData.plot.barh(y='counts', x='app id', color='#9a6bd1')

#plt.pie([pieData[0], pieData[1]], labels=['fraudulent', 'benign'], startangle=27, explode=[0, 0.1], colors=['c', 'r'])
plt.show()
#"""