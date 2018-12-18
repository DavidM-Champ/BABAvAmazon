# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 19:38:39 2018

@author: David
"""

import pandas as pd
import matplotlib.pyplot as plt

print("Shopify:\n")

gdp=pd.read_csv("GDP-data.csv")
shop_df=pd.read_csv("SHOP-earnings.csv")
shop_price=pd.read_csv("SHOP.csv")

new_df=shop_df.drop(['Quarter'],axis=1)

for column in new_df.columns:
    print(column)
    corr=shop_price['Close'].corr(new_df[column])
    print(corr)

new_gdp=gdp.drop(['Quarter'],axis=1)

for column in new_gdp.columns:
    print(column)
    corr=shop_price['Close'].corr(new_gdp[column])
    print(corr)
    
delayed_gdp=new_gdp.iloc[:-2,:]
    
print("\nDelayed GDP:")
for column in delayed_gdp.columns:
    print(column)
    corr=shop_price['Close'].corr(delayed_gdp[column])
    print(corr)

f, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(shop_df['Quarter'],shop_df['Revenues'])
f.suptitle('Shopify Revenues vs Price', fontsize=16)
ax2.plot(shop_price['Close'])

f, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(shop_df['Quarter'],shop_df['Total-Assets'])
f.suptitle('Shopify Assets vs Price', fontsize=16)
ax2.plot(shop_price['Close'])

f, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(gdp['Quarter'],gdp['USA-GDP-GROWTH'])
f.suptitle('USA GDP Growth vs Shopify Price', fontsize=16)
ax2.plot(shop_price['Close'])

#Made to test if correlations are higher or lower
print("\nReduced datasets (2017 and before):\n")
#Reduced datasets
shop_df=pd.read_csv("SHOP-earnings-reduced.csv")
shop_price=pd.read_csv("SHOP-reduced.csv")

new_df=shop_df.drop(['Quarter'],axis=1)

for column in new_df.columns:
    print(column)
    corr=shop_price['Close'].corr(new_df[column])
    print(corr)

new_gdp=gdp.drop(['Quarter'],axis=1)

for column in new_gdp.columns:
    print(column)
    corr=shop_price['Close'].corr(new_gdp[column])
    print(corr)
    
    
print("\n\nAlibaba:\n")

baba_df=pd.read_csv("BABA-earnings.csv")
baba_price=pd.read_csv("BABA.csv")

new_df=baba_df.drop(['Quarter'],axis=1)

for column in new_df.columns:
    print(column)
    corr=baba_price['Close'].corr(new_df[column])
    print(corr)

for column in new_gdp.columns:
    print(column)
    corr=baba_price['Close'].corr(new_gdp[column])
    print(corr)
    
print("\nDelayed GDP:")
for column in delayed_gdp.columns:
    print(column)
    corr=baba_price['Close'].corr(delayed_gdp[column])
    print(corr)
    
f, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(baba_df['Quarter'],baba_df['Revenues'])
f.suptitle('Alibaba Revenues vs Price', fontsize=16)
ax2.plot(baba_price['Close'])

f, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(baba_df['Quarter'],baba_df['Total-Assets'])
f.suptitle('Alibaba Assets vs Price', fontsize=16)
ax2.plot(baba_price['Close'])

f, (ax1, ax2) = plt.subplots(1, 2)
f.suptitle('Chinese GDP Growth vs Alibaba Price', fontsize=16)
ax1.plot(gdp['Quarter'],gdp['CHINA-GDP-GROWTH'])
ax2.plot(baba_price['Close'])

f, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(gdp['Quarter'],gdp['USA-GDP-GROWTH'])
ax2.plot(baba_price['Close'])
    
print("\nReduced datasets (2017 and before):\n")

baba_price=pd.read_csv("BABA-reduced.csv")
baba_df=baba_df.iloc[:-3,:]

new_df=baba_df.drop(['Quarter'],axis=1)

for column in new_df.columns:
    print(column)
    corr=baba_price['Close'].corr(new_df[column])
    print(corr)
    
print("\n\nAmazon:\n")

amzn_df=pd.read_csv("AMZN-earnings.csv")
amzn_price=pd.read_csv("AMZN.csv")

new_df=amzn_df.drop(['Quarter'],axis=1)

for column in new_df.columns:
    print(column)
    corr=amzn_price['Close'].corr(new_df[column])
    print(corr)

for column in new_gdp.columns:
    print(column)
    corr=amzn_price['Close'].corr(new_gdp[column])
    print(corr)
    
print("\nDelayed GDP:")
for column in delayed_gdp.columns:
    print(column)
    corr=amzn_price['Close'].corr(delayed_gdp[column])
    print(corr)
    
f, (ax1, ax2) = plt.subplots(1, 2)
f.suptitle('Amazon Net Sales vs Price', fontsize=16)
ax1.plot(amzn_df['Quarter'],amzn_df['Net-sales'])
ax2.plot(amzn_price['Close'])

f, (ax1, ax2) = plt.subplots(1, 2)
f.suptitle('Amazon Assets vs Price', fontsize=16)
ax1.plot(amzn_df['Quarter'],amzn_df['Total-Assets'])
ax2.plot(amzn_price['Close'])

f, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(gdp['Quarter'],gdp['CHINA-GDP-GROWTH'])
ax2.plot(amzn_price['Close'])

f, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(gdp['Quarter'],gdp['USA-GDP-GROWTH'])
ax2.plot(amzn_price['Close'])