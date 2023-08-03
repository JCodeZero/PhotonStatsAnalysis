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

length = 5
edgesx = np.empty((0,1))
means = np.empty((0,1))
stds = np.empty((0,1))
topy = np.empty((0,1))
bottomy = np.empty((0,1))
for i in range(int((time[-1] - time[0])/length)):
    edgesx = np.append(edgesx, np.array([[time[0] + length*i]]))
    means = np.append(means, np.array([[np.mean(photons[length*i:length*(i+1)])]]))
    std = np.std(photons[length*i:length*(i+1)])
    stds = np.append(stds, np.array([[std]]))
    topy = np.append(topy, np.array([[np.mean(photons[length*i:length*(i+1)]) + 3 * std]]))
    bottomy = np.append(bottomy, np.array([[np.mean(photons[length*i:length*(i+1)]) - 3 * std]]))
    
edgesx = np.append(edgesx, np.array([[edgesx[-1] + length]]))
means = np.append(means, np.array([[means[-1]]]))
stds = np.append(stds, np.array([[stds[-1]]]))
topy = np.append(topy, np.array([[topy[-1]]]))
bottomy = np.append(bottomy, np.array([[bottomy[-1]]]))

start = []
end = []
for i in range(len(edgesx) - 1):
    if means[i+1] > topy[i]:
        start.append(timearray[5*i])

for i in range(len(edgesx) - 1):
    if means[i+1] < bottomy[i]:
        end.append(timearray[5*i])

comparemethod = filterdat[(filterdat['TIME']>start[0]) & (filterdat['TIME']<end[-1])]

_=plt.hist(comparemethod['TIME'], bins=300)
plt.xlabel('Time (s)')
plt.ylabel('# of photons')
plt.show()
