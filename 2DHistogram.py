import sys
from astropy.io import fits
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.widgets import Slider

filename = sys.argv[1]
eventfile=fits.open(filename)
events=eventfile[1].data
shortdat=events[(events['TIME']>660920900) & (events['TIME']<660921200)]
cleanevts = shortdat[(shortdat['EVENT_FLAGS']==0) & (shortdat['ENERGY']>15)]
filterdat = shortdat[(shortdat['EVENT_FLAGS']==0) & (shortdat['ENERGY']>15)]

array = np.empty((0,2), int)
time = []

df = pd.DataFrame(filterdat, columns = ['TIME','DET_ID','EVENT_FLAGS','PHA','MASK_WEIGHT','DETX','DETY','PI','ENERGY'])
df['TIME'] = df['TIME'].apply(lambda x: round(x))
time.extend(df['TIME'].tolist())

for i in range(len(time)):
    if int(time[i]) == time[0]:
        array = np.append(array, np.array([[int(df.iloc[i][5]), int(df.iloc[i][6])]]), axis=0)

df2 = pd.DataFrame(array, columns=['DETX', 'DETY'])
#-------------------------------------------------------------------------------------
init_x=df2['DETX']
init_y=df2['DETY']

fig, ax = plt.subplots()
hist = ax.hist2d(x=init_x, y=init_y, bins=100, cmap='afmhot')
plt.xlabel('DETX')
plt.ylabel('DETY')
fig.subplots_adjust(bottom=0.25)

cbar = fig.colorbar(hist[3], ax=ax)
cbar.ax.get_yaxis().labelpad = 20
cbar.set_label('# Photons in Bin', rotation=270)
cbar.mappable.set_clim(vmin=0, vmax=25)

axtime = fig.add_axes([0.15, 0.1, 0.65, 0.03])
time_slider = Slider(
    ax=axtime,
    label='Time [s]',
    valmin=time[0],
    valmax=time[-1],
    valinit=time[0], valstep=1,
)

def update(val):
    newx = np.empty((0,1), int)
    newy = np.empty((0,1), int)
    for i in range(len(time)):
        if int(time[i]) == time_slider.val:
            newx = np.append(newx, np.array([[int(df.iloc[i][5])]]))
            newy = np.append(newy, np.array([[int(df.iloc[i][6])]]))
    ax.clear()
    hist = ax.hist2d(x=newx, y=newy, bins=100, cmap='afmhot')
    fig.canvas.draw_idle()


time_slider.on_changed(update)


plt.show()
