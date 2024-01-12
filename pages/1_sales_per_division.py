import streamlit as st
import pandas as pd


dataset_path ='../transactions.csv'
df = pd.read_csv(dataset_path)
st.title('Sales per Division')

chart_data = df.groupby('DIVISION', as_index=False)['QUANTITY_SOLD'].count()

st.bar_chart(chart_data,  x="DIVISION", y=['QUANTITY_SOLD'])
