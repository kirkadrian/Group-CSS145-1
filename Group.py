import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("GROUP 4")
st.header("Laptop Prices Dataset")

df = pd.read_csv("dataset/laptop_price.csv")

df.head(10)

nbins = int(np.sqrt(len(df)))

plt.figure(figsize=(10, 8))
plt.hist(df['Price (Euro)'], bins=nbins, edgecolor='black')

plt.title('Distribution of Laptop Prices', fontsize=12, fontweight='bold')
plt.xlabel('Price (Euro)')
plt.ylabel('Frequency')

st.pyplot(plt)