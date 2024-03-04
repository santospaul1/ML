from sklearn.datasets import make_moons
from matplotlib import pyplot as plt
from matplotlib import style

style.use("fivethirtyeight")

x,y = make_moons(n_samples= 1000, noise=0.1)
 
plt.scatter(x[:, 0], x[:, 1], s=40, color = 'g')
plt.ylabel("y")
plt.xlabel("x")

plt.show()
plt.clf