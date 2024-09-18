import numpy as np
from sklearn.model_selection import train_test_split
dataset = np.arange(10)
result = train_test_split(dataset)
print(dataset)
print(result)
