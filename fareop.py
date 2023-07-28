# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 09:38:16 2019

@author: Nachiket
"""
import pyrebase as pb
config={"apiKey": "AIzaSyB4s-zOO50DyIduVkWWYb9c6c1DT97VBqg",
    "authDomain": "myshop-76cba.firebaseapp.com",
    "databaseURL": "https://myshop-76cba.firebaseio.com",
    "projectId": "myshop-76cba",
    "storageBucket": "",
    "messagingSenderId": "187498078910",
    "appId": "1:187498078910:web:29abd27a8f762f6b0174ef"
      }
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from math import radians, sin, cos, acos
import pandas as pd

from itertools import tee
df = pd.read_csv('C:/Users/Nachiket/Desktop/cabtime3.csv', sep=',')
x=df['longitude'].values
y=df['latitude'].values
X=np.array(list(zip(x,y)))
kmeans = KMeans(n_clusters=11)
kmeans.fit(X)

i=0
while i<50:
    i=i+1
    firebase=pb.initialize_app(config)
    x=firebase.database().child("College").get()
    y=firebase.database().child("College")
    z=firebase.database().child("College")
    w=firebase.database().child("College")
    cc=[]
    
    ab=firebase.database()
    for u in x.each():
        cc.append(u.val())
    print(cc[2])
    if cc[2]==1:
        lat=y.child("mycor").child("lat").get().val()
        lon=z.child("mycor").child("long").get().val()
        slat=radians(lat)
        slon=radians(lon)
        #print(lat)
        #print(lon)
        ab.child("College").child("sample").remove()
        w.child("id").set(0)
        db=firebase.database().child("College")
        ab=firebase.database()
        ans={"ans":cc[0]/2}
        db.child("ans").set(cc[0]/2)               
        cl=[]       
        cl=kmeans.cluster_centers_
        count=0
        for l in cl:
            dist = 6371.01 * acos(sin(slat)*sin(radians(l[0])) + cos(slat)*cos(radians(l[0]))*cos(slon - radians(l[1])))
            if dist<1:
                d={"lan":l[0],"lon":l[1]}
                ab.child("College").child("sample").child("cor").child(count).set(d)
                count=count+1
                print(l)
    if cc[2]==99:
        break
