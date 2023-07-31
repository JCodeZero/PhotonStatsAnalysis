import sys
from astropy.io import fits

filename = sys.argv[1]
eventfile=fits.open('filename')
events=eventfile[1].data

import matplotlib.pyplot as plt

shortdat=events[(events['TIME']>660920900) & (events['TIME']<660921200)]
shorterdat = events[(events['TIME']>660921026) & (events['TIME']<660921120)]

_=plt.hist(shorterdat['TIME'],bins=1000)
plt.xlabel('Time (s)')
plt.ylabel('# of photons')
plt.show()
