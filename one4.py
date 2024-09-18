import numpy as np
from sklearn.model_selection import train_test_split
dataset = np.arange(10)
X_train,X_test = train_test_split(dataset)
print(dataset)
print()
print(X_test)