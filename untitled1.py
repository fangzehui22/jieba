import numpy as np
import matplotlib.pyplot as plt
fracs = [3,1,1,1,1]
labels = 'goupiao', 'lishi', 'ganxingqu','remen','pingfen'
explode = [ 0.1,0,0,0,0]
plt.axes(aspect=1)
plt.pie(x=fracs, labels=labels, explode=explode,autopct='%3.1f %%',
        shadow=True, labeldistance=1.1, startangle = 90,pctdistance = 0.6)
plt.show()
