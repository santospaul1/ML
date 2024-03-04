#import the necessary libraries
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

# generate 2d classification dataset
X, y = make_classification(n_samples = 100, 
						n_features=2,
						n_redundant=0,
						n_informative=2,
						n_repeated=0,
						n_classes =3,
						n_clusters_per_class=1)

# Plot the generated datasets
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()
#plt.clf
