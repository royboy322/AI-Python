# rabbit hole:
# gradient descent sometimes has the tendency to inviting an issue of overflow.
# because you may find yourself doing division of 0/0 when computing gradient (derivatives).
# https://stackoverflow.com/questions/7559595/python-runtimewarning-overflow-encountered-in-long-scalars
import numpy as np


class GradientDescentLinearRegression:
    def __init__(self, learning_rate=0.0001, iterations=10000):
        self.learning_rate, self.iterations = learning_rate, iterations

    def fit(self, X, y):
        b = 1.5
        m = 3.0
        n = X.shape[0]
        for _ in range(self.iterations):
            b_gradient = -2 * np.sum(y - m * X - b) / n
            m_gradient = -2 * np.sum(X * (y - (m * X + b))) / n
            b = b - (self.learning_rate * b_gradient)
            m = m - (self.learning_rate * m_gradient)
        self.m, self.b = m, b
        return m, b

    def predict(self, X):
        return self.m * X + self.b


if __name__ == "__main__":
    np.random.seed(42)

    X = np.linspace(0, 100, 1000) + np.random.normal(loc=0, size=1000, scale=10)
    Y = 3 * X + 1.5 + np.random.normal(loc=0, size=1000, scale=0.1)

    #learning rate experiments
    for learning_rate in [1, 0.1, 0.01]:
        clf = GradientDescentLinearRegression(learning_rate=learning_rate)
        m, b = clf.fit(X, Y)
        print(f"Learning rate: {learning_rate}, m: {m}, b: {b}")

        #plot results
        import matplotlib.pyplot as plt

        plt.style.use('fivethirtyeight')
        plt.scatter(X, Y, color='black', s=10, label='Data points')
        plt.plot(X, clf.predict(X), label=f'LR={learning_rate}')
        plt.gca().set_title(f"Gradient Descent Linear Regressor (LR={learning_rate})")
        plt.legend()
        plt.show()

    #observations:
    #learning rate = 1, the estimates for m and b might diverge or oscillate.
    #learning rate = 0.1, the estimates for m and b might converge but can be unstable.
    #learning rate = 0.01, the estimates for m and b are more stable and closer to the true values.
    #improvement happens as the learning rate decreases because it allows for smaller and controlled steps toward the minimum of the cost function. Too high a learning rate can cause overshooting, while too low a learning rate can slow down the convergence.
    #recommendation, we must use a learning rate that is small enough to ensure stability but large enough to allow the algorithm to converge in a reasonable amount of time. 0.01 seems to be a good choice here.

    #iterations experiments
    learning_rate = 0.001
    for iterations in [2, 10, 1000]:
        clf = GradientDescentLinearRegression(learning_rate=learning_rate, iterations=iterations)
        m, b = clf.fit(X, Y)
        print(f"Learning rate: {learning_rate}, Iterations: {iterations}, m: {m}, b: {b}")

        #plot results
        plt.scatter(X, Y, color='black', s=10, label='Data points')
        plt.plot(X, clf.predict(X), label=f'Iters={iterations}')
        plt.gca().set_title(f"Gradient Descent Linear Regressor (Iters={iterations})")
        plt.legend()
        plt.show()

    #observations:
    #the iterations = 2, the estimates for m and b are far from the true values because the model hasn't had enough time to stablize.
    #the iterations = 10, the estimates for m and b improve but are still not very accurate.
    #the iterations = 1000, the estimates for m and b are much closer to the true values, indicating better convergence.
    #for more iterations we have to allow the model to refine its estimates, leading to better convergence. However, too many iterations can lead to overfitting and increased computational cost.
