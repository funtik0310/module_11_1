import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.DataFrame({'A': [1, 2, 3]})
print(s)

s_ = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s_)

x = [1, 2, 3, 4, 5]
y = [25, 32, 34, 20, 25]

plt.plot(x, y)
plt.xlabel('Ось х')
plt.ylabel('Ось y')
plt.title('График')
plt.plot(x, y, color='green', marker='o', markersize=7)
plt.show()
