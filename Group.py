import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("GROUP 4")
st.header("Laptop Prices Dataset")

df = pd.read_csv("dataset/laptop_price.csv")

#Manalang 1

df.head(10)

nbins = int(np.sqrt(len(df)))

plt.figure(figsize=(10, 8))
plt.hist(df['Price (Euro)'], bins=nbins, edgecolor='black')

plt.title('Distribution of Laptop Prices', fontsize=12, fontweight='bold')
plt.xlabel('Price (Euro)')
plt.ylabel('Frequency')

st.pyplot(plt)

#Manalang 2

data = df['TypeName'].value_counts()

custom_order = ['Notebook', 'Gaming', 'Ultrabook', 'Netbook', '2 in 1 Convertible', 'Workstation']

data = data.reindex(custom_order).fillna(0)

color = ['#7AD9F8', '#A8D600', '#F15A5E', '#D46783', '#FFB84D', '#B47FC1']

explode = [0.05] * len(data)

plt.figure(figsize=(10, 8))
plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=40, colors=color, explode=explode, shadow=True, wedgeprops={'edgecolor':'black', 'linewidth' : 0.5, 'antialiased' : True})

plt.title('Distribution of Laptop Types', fontsize=12, fontweight='bold')

plt.axis('equal')
plt.show()
