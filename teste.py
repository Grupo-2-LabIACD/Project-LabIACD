import numpy as np
treenumber=[50,100,150,200,250]
values=[0.6,0.7,0.3,0.8,0.77]




values=np.array(values)
index=np.where(values==np.max(values))
besttree=treenumber[index[0][0]]
print(f"Best tree value={besttree}")