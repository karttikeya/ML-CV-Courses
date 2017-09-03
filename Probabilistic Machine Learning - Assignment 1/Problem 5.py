
# coding: utf-8

# In[4]:

import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
import scipy.stats
from scipy.stats import multivariate_normal

x= np.array( [ -2.23, -1.30, -0.42, 0.30, 0.33, 0.52, 0.87, 1.80, 2.74, 3.62]).reshape((-1,1))
y = np.array([1.01, 0.69, -0.66, -1.34, -1.75, -0.98, 0.25, 1.57, 1.65, 1.51]).reshape((-1,1))

def transform(data,k): # CONSTRUCTS A Matrix of len(data)x(K+1) shape with the transformation [1 x x^2 .. x^K]
    transformed = list()
    for num in data:
        eachpoint = list()
        for power in range(k+1):
            eachpoint.append(pow(num,power))
        transformed.append(eachpoint)
    transformed = np.array(transformed).squeeze()
    return transformed


k = 1 #Set value at k

transformed = transform(x,k)
inner_term = inv(np.dot(transformed.T,transformed) + 0.25*np.identity(k+1))  #Calulcating the mean and var for posterior
mean = np.dot(np.dot(inner_term,transformed.T),y)
xplot = np.linspace(-4,4,100)
xplottransformed = transform(xplot,k)  #transofrming plot points.

std = inv(4*np.dot(transformed.T,transformed) + np.identity(k+1))
xplotstd = np.array([np.dot(np.dot(x.T,std),x)+0.25 for x in xplottransformed]).reshape(-1,1)  #Eval var at plot points

res = np.dot(xplottransformed,mean)

plt.plot(xplot,res, label = "Predicitve Posterior")
plt.plot(x,y,'x', label = "points")
plt.plot(xplot, res + 2*xplotstd , label = "upper std envelope")  #Plotting the upper and the lower envelopes.
plt.plot(xplot, res - 2*xplotstd , label = "lower std envelope")
plt.legend(loc='upper right')
plt.title('Likelihood for range [-4,4] for K= 1')
plt.show()


std = inv(4*np.dot(transformed.T,transformed) + np.identity(k+1))

var = np.dot(transformed,transformed.T) + 0.25*np.identity(transformed.shape[0])
dis = multivariate_normal(mean=np.zeros(transformed.shape[0]), cov=var)

print('The marginal likelihood for the model is:',dis.pdf(y.T))

print(max(xplotstd),np.argmax(xplotstd)) #This shows that -4 has the highest variance and hence is suitable for a new point


# In[ ]:



