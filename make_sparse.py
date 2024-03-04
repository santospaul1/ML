# Import necessary libraries
from sklearn.datasets import make_sparse_uncorrelated
import matplotlib.pyplot as plt
# Generate 1d Regression dataset 
X, y = make_sparse_uncorrelated(n_samples = 100, n_features=4, random_state=23)
# Plot the generated datasets
plt.figure(figsize=(12,10))
for i in range(4):
	plt.subplot(2,2, i+1)
	plt.scatter(X[:,i], y)
	plt.xlabel('X'+str(i+1))
	plt.ylabel('Y')
plt.show()
