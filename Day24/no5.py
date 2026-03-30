import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

mu =28
sigma = 15
samples = 100_000

x = np.random.normal(mu,sigma,samples)
ax = sns.displot(x)
ax.set(xlabel="Nilai x",ylabel="Nilai y")
plt.show()