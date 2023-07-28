import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans


distance=2
 #i=0,j=0
import pandas as pd

from itertools import tee

#Read CSV file into dataframe named 'df'
#change seperator (sep e.g. ',') type if necessary
df = pd.read_csv('C:/Users/HP/Desktop/cabtime3.csv', sep=',')




x=df['longitude'].values
y=df['latitude'].values
X=np.array(list(zip(x,y)))


plt.scatter(X[:,0],X[:,1], label='True Position')

kmeans = KMeans(n_clusters=11)
kmeans.fit(X)

print(kmeans.cluster_centers_)

plt.scatter(X[:,0],X[:,1], c=kmeans.labels_, cmap='rainbow')
