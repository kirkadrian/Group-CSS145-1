import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

uploaded_file = st.file_uploader("Insert laptop_price.csv here", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    nbins = int(np.sqrt(len(df)))

    plt.figure(figsize=(10, 8))
    plt.hist(df['Price (Euro)'], bins=nbins, edgecolor='black')

    plt.title('Distribution of Laptop Prices', fontsize=12, fontweight='bold')
    plt.xlabel('Price (Euro)')
    plt.ylabel('Frequency')

    st.pyplot(plt)
else:
    st.write("Please upload the CSV file.")
