import sys
from astropy.io import fits
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

filename = sys.argv[1]
eventfile=fits.open('filename')
events=eventfile[1].data
shortdat=events[(events['TIME']>660920900) & (events['TIME']<660921200)]
cleanevts = shortdat[(shortdat['EVENT_FLAGS']==0) & (shortdat['ENERGY']>15)]
filterdat = shortdat[(shortdat['EVENT_FLAGS']==0) & (shortdat['ENERGY']>15)]

time = []

df = pd.DataFrame(filterdat, columns = ['TIME','DET_ID','EVENT_FLAGS','PHA','MASK_WEIGHT','DETX','DETY','PI','ENERGY'])
df['TIME'] = df['TIME'].apply(lambda x: round(x))
time.extend(df['TIME'].tolist())

photons = np.empty((0,1), int)
temp = 0

timearray = np.array(list(range(time[0], time[-1])))
    

for i in timearray:
    for j in range(len(time)):
        if time[j] == i:
            temp = temp + 1
    photons = np.append(photons, np.array([[temp]]))
    temp = 0

sum = 0
count = 0
for i in range(len(photons) - 1):
    if photons[i+1] - photons[i] < 2000:
        sum = sum + photons[i]
        count = count + 1

avg = sum/count
temparray = np.empty((0,2), int)

for i in range(len(photons)):
    if photons[i] > avg:
        temparray = np.append(temparray, np.array([timearray[i]]))

slopemethod = filterdat[(filterdat['TIME']>temparray[0]) & (filterdat['TIME']<temparray[-1])]

_=plt.hist(slopemethod['TIME'], bins=300)
plt.xlabel('Time (s)')
plt.ylabel('# of photons')
