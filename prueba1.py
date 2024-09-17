import time

import matplotlib.pyplot as plt
import numpy as np
import random

colors = ['binary', 'gist_yarg', 'gist_gray', 'gray', 'bone',
            'pink', 'spring', 'summer', 'autumn', 'winter', 'cool',
             'Wistia', 'hot', 'afmhot', 'gist_heat', 'copper']
while True:

    p = random.choice(plt.colormaps())
    p2 = random.choice(colors)

    plt.figure()
    plt.pcolormesh(np.random.rand(20,20), cmap=p2)
    plt.show()
    time.sleep(5)