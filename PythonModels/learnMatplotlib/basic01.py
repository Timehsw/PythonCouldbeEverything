import matplotlib.pyplot as plt
from numpy.random import randn
import numpy as np
fig=plt.figure()

ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)

plt.plot(randn(50).cumsum(),'ko--')

_=ax1.hist(randn(100),bins=20,color='k',alpha=0.3)
ax2.scatter(np.arange(30),np.arange(30)+3*randn(30))
plt.show()

