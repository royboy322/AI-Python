import numpy as np
import matplotlib.pyplot as plt

#generate data
X = np.linspace(0, 10, 1000) + np.random.normal(loc=0, scale=0.1, size=1000)
Y = 4 * X + 15 + np.random.normal(loc=0, scale=10, size=1000)

#plot the data
plt.scatter(X, Y, alpha=0.5)
plt.xlabel("Years of Education")
plt.ylabel("Income (in thousand dollars)")
plt.title("Income vs. Years of Education")
plt.show()

# Comment:
# The plot shows a positive linear relationship between income and years of education, as expected.
# The scatter plot shows that as the years of education increase, the income also tends to increase.
# However, there is some noise due to the error term, which makes the data points scattered around the line.

#adjusting scale of noise and plotting
scales = [0.1, 1, 10]
for scale in scales:
    X = np.linspace(0, 10, 1000) + np.random.normal(loc=0, scale=0.1, size=1000)
    Y = 4 * X + 15 + np.random.normal(loc=0, scale=scale, size=1000)
    plt.scatter(X, Y, alpha=0.5, label=f'scale={scale}')

plt.xlabel("Years of Education")
plt.ylabel("Income (in thousand dollars)")
plt.title("Income vs. Years of Education with Different Scales of Noise")
plt.legend()
plt.show()

# Comments on findings:
# When the scale of the noise is 0.1, the data points are tightly clustered around the line, showing a clear linear relationship.
# When the scale of the noise is 1, the data points are more spread out, but the linear relationship is still noticeable.
# When the scale of the noise is 10, the data points are widely scattered, making the linear relationship less apparent.
# As the scale increases, the variance in the income data increases, causing the points to scatter more widely.
