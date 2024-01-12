import streamlit as st
import pandas as pd


dataset_path ='../transactions.csv'
df = pd.read_csv(dataset_path)
st.title('Sales per PRODUCT_CATEGORY')

chart_data = df.groupby('PRODUCT_CATEGORY', as_index=False)['QUANTITY_SOLD'].count()

# print(chart_data)
st.bar_chart(chart_data,  x="PRODUCT_CATEGORY", y=['QUANTITY_SOLD'])
