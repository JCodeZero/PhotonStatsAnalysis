from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.widgets import Slider
#-------------------------------------------------------------------------------------
filename = 'sw01088940000bevshsp_uf.evt.gz'
eventfile=fits.open(filename)
events=eventfile[1].data
shortdat=events[(events['TIME']>660920900) & (events['TIME']<660921200)]
filterdat = shortdat[(shortdat['EVENT_FLAGS']==0) & (shortdat['ENERGY']>0)]

#-------------------------------------------------------------------------------------
array = np.empty((0,3), int)
index = -1
time = []

df = pd.DataFrame(filterdat, columns = ['TIME','DET_ID','EVENT_FLAGS','PHA','MASK_WEIGHT','DETX','DETY','PI','ENERGY'])
df['TIME'] = df['TIME'].apply(lambda x: round(x))
time.extend(df['TIME'].tolist())

for i in time:
    if int(i) == df['TIME'][0]:
        index = index + 1
        array = np.append(array, np.array([[int(df.iloc[index][5]), int(df.iloc[index][6]), int(df.iloc[index][8])]]), axis=0)

df2 = pd.DataFrame(array, columns=['DETX', 'DETY', 'ENERGY'])

#-------------------------------------------------------------------------------------
Xmax = 0
Ymax = 0

for i in df2['DETX']:
    if i > Xmax:
        Xmax = i

for i in df2['DETY']:
    if i > Ymax:
        Ymax = i
        
def round50(x, base=50):
    return base * round(x/base)
    
Xmax = round50(Xmax, base=25) + 25
Ymax = round50(Ymax, base=25) + 25
        
#-------------------------------------------------------------------------------------
fig, ax = plt.subplots()
scat = ax.scatter(df2['DETX'], df2['DETY'], df2['ENERGY'], alpha=0.5)
plt.xlim([-10, Xmax])
plt.ylim([-10, Ymax])

fig.subplots_adjust(bottom=0.25)

#The horizontal slider for time
axtime = fig.add_axes([0.15, 0.1, 0.65, 0.03])
time_slider = Slider(
    ax=axtime,
    label='Time [s]',
    valmin=time[0],
    valmax=time[-1],
    valinit=time[0], valstep=1,
)
    
# The function to be called anytime a slider's value changes
def update(val):
    newx = np.empty((0,1), int)
    newy = np.empty((0,1), int)
    newsize = np.empty((0,1), int)
    for i in range(len(time)):
        if int(time[i]) == time_slider.val:
            newx = np.append(newx, np.array([[int(df.iloc[i][5])]]), axis=0)
            newy = np.append(newy, np.array([[int(df.iloc[i][6])]]), axis=0)
            newsize = np.append(newsize, np.array([[int(df.iloc[i][8])]]), axis=0)
    ax.clear()
    scat = ax.scatter(newx, newy, newsize, alpha=0.5)
    fig.canvas.draw_idle()


# register the update function with each slider
time_slider.on_changed(update)


plt.show()


# In[ ]:




