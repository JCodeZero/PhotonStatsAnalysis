import sys
from astropy.io import fits
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

filename = sys.argv[1]
eventfile=fits.open(filename)
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

bins,ns=np.histogram(shortdat['TIME'],bins=300)
plt.plot(ns[:-1],bins)
