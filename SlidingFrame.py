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

intervals = pd.DataFrame(columns = ['START', 'END', 'COUNTMEAN'])
maxstart = []
maxend = []
maxmean = []
for i in range(len(timearray)):
    tempstartlist = []
    tempendlist = []
    tempmeanlist = []
    
    for j in range(0, time[-1] - time[0]):
        if j+i+1 <= 300:
            tempstartlist.append(j)
            tempendlist.append(j+i+1)
            tempmeanlist.append(np.mean(photons[j:j+i+1]))
    
    for i in range(len(tempstartlist)):
        if tempmeanlist[i] == np.max(tempmeanlist):
            maxstart.append(tempstartlist[i])
            maxend.append(tempendlist[i])
            maxmean.append(tempmeanlist[i])
    
intervals['START'] = maxstart
intervals['END'] = maxend
intervals['COUNTMEAN'] = maxmean

freqstart = np.argmax(np.bincount(intervals['START']))
freqend = 0

for i in range(len(maxstart)):
    if intervalranges['START'][i] == freqstart:
        if intervals['ErangeND'][i] > freqend:
            freqend = intervals['END'][i]
            
slidemethod = filterdat[(filterdat['TIME']>timearray[freqstart]) & (filterdat['TIME']<timearray[freqend])]

_=plt.hist(slidemethod['TIME'], bins=300)
plt.xlabel('Time (s)')
plt.ylabel('# of photons')
