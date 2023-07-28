# Importing Necessary Libraries
 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (20.0, 10.0)
 
# Reading Data
data = pd.read_csv('F:\ccd.csv')
print(data.price)
data.head()

 
 
# Collecting X and Y
X = data['distance'].values
Y = data['price'].values

mean_x = np.mean(X)
mean_y = np.mean(Y)
 
# Total number of values
n = len(X)
 
# Using the formula to calculate m and c
numer = 0
denom = 0
for i in range(n):
    numer += (X[i] - mean_x) * (Y[i] - mean_y)
    denom += (X[i] - mean_x) ** 2    
m = numer / denom
c = mean_y - (m * mean_x)         
# Print coefficients
print(m, c)

# Plotting Values and Regression Line
max_x = np.max(X) + 100
min_x = np.min(X) - 100
# Calculating line values x and y
x = np.linspace(min_x, max_x, 1000)
y = c + m * x 
 
# Ploting Line
plt.plot(x, y, color='#52b920', label='Regression Line')
# Ploting Scatter Points
plt.scatter(X, Y, c='#ef4423', label='Scatter Plot')
 
plt.xlabel('Distance')
plt.ylabel('Price')
plt.xlim(0,5)
plt.ylim(0,55)
plt.legend()
plt.show()

f=m*4+c
g=m*1+c
print('Max Fare=',f)
print('Max Fare=',g)






