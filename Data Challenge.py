# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 12:25:28 2019

@author: Shloak
"""
import pandas as pd 
import matplotlib.pyplot as plt

df1 = pd.read_csv("MSA1.csv")
df2 = pd.read_csv("MSA2.csv")

#df1.head()
#df2.head()

#Finding No. of Properties Sold After 2018
df1x = df1[df1["Apr-08"] != "S"]
df1x = df1x[df1x["Apr-08"] != "R"]
df1x[["Apr-08"]] 
df1x.shape
df1xs = df1x[df1x["Status"] == "S"]
df1xr = df1x[df1x["Status"] == "R"]


print("No. of properties that are sold after April-08 in Akron/Ohio =" , df1xs.shape[0]+df1xr.shape[0])


df2x = df2[df2["Apr-08"] != "S"]
df2x = df2x[df2x["Apr-08"] != "R"]
df2x[["Apr-08"]] 
df2x.shape
df2xs = df2x[df2x["Status"] == "S"]
df2xr = df2x[df2x["Status"] == "R"]

print("No. of properties that are sold after April-08 in Austin/Texas =", df2xs.shape[0]+df2xr.shape[0])


#Finding Average Time from Lease Up to Sale
df1.columns[27:]
ct=0
for x in df1x.columns[27:]:
    y=df1x[df1x[x] == "LU"]
    ct=ct+y.shape[0]

print("Average time taken for Lease up time in Market Akron/Ohio",ct/df1x.shape[0],"months")


df2.columns[27:]
ct=0
for x in df2x.columns[27:]:
    y=df2x[df2x[x] == "LU"]
    ct=ct+y.shape[0]

print("Average time taken for Lease up time in Market Austin/Texas",ct/df2x.shape[0],"months")

## It is observed that that properties in Ohio have sgnificantly less Lease Up time than properties in Texas


# Finding effective increase in rent per square feet
df3 = pd.read_csv("effective rent msa1.csv")
df3.columns[27:]
print(df3.dropna(subset=["Apr-08"])[["Apr-08"]])


ct=0
avgs1=[]
dates1=df3.columns[27:]
for x in df3.columns[27:]:
    y=df3.dropna(subset=[x])
    avgs1.append(y[x].mean())
        
x = dates1
y = avgs1
xn=[]
yn=[]
for m,val in enumerate(x):
    if m%4==0:
        xn.append(val)
        yn.append(y[m])
        
plt.plot(xn, yn)
plt.xticks(rotation=90)
#plt.figure(figsize=(6,6)) 
plt.xlabel('Change Over Quaters', fontsize=16)
plt.ylabel('Average per sq foot price', fontsize=16)
plt.show()


#Took into account the Price variation in rent with every quater. 
#Almost a 50 percent increase can be observed in Rent per sqaure feet in Ohio since 2009

#
#
#
df4 = pd.read_csv("effective rent msa2.csv")
df4.columns[27:]
print(df4.dropna(subset=["Apr-08"])[["Apr-08"]])


ct=0
avgs1=[]
dates1=df4.columns[27:]
for x in df4.columns[27:]:
    y=df4.dropna(subset=[x])
    avgs1.append(y[x].mean())
        
x = dates1
y = avgs1
xn=[]
yn=[]
for m,val in enumerate(x):
    if m%4==0:
        xn.append(val)
        yn.append(y[m])
        
plt.plot(xn, yn)
plt.xticks(rotation=90)
#plt.figure(figsize=(6,6)) 
plt.xlabel('Change over Quaters', fontsize=16)
plt.ylabel('Average per sq foot price', fontsize=16)
plt.show()
  
#Almost a 50 percent increase can be observed in Rent per sqaure feet in Texas since 2009
#Using These graphs we can predict the increase in prices in future