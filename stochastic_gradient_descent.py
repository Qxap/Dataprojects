import numpy as np

np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

X_b = np.c_[np.ones((100, 1)), X]
theta = np.random.randn(2, 1)

eta = 0.1
n_epochs = 50

for epoch in range(n_epochs):
    for i in range(len(X_b)):
        rand_i = np.random.randint(len(X_b))
        xi = X_b[rand_i:rand_i+1]
        yi = y[rand_i:rand_i+1]
        gradients = 2 * xi.T.dot(xi.dot(theta) - yi)
        theta = theta - eta * gradients

print(theta)