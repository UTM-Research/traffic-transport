import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
index = []
columns = []
df = DataFrame(abs(np.random.randn(5, 4)), index=index, columns=columns)
plt.pcolor(df)
plt.colorbar()
plt.yticks(np.arange(0.5, len(df.index), 1), df.index)
plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns)
plt.show()



