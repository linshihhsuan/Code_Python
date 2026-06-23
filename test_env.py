import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

print("NumPy version:", np.__version__)
print("Pandas version:", pd.__version__)
print("Scikit-learn version:", sklearn.__version__)

x = np.array([1, 2, 3, 4, 5])
y = x ** 2

plt.plot(x, y)
plt.title("test plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

print("Success")