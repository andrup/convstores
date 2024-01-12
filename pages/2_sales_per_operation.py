import streamlit as st
import pandas as pd


dataset_path ='../transactions.csv'
df = pd.read_csv(dataset_path)
st.title('Sales per Operation')

chart_data = df.groupby('OPERATION_ID', as_index=False)['QUANTITY_SOLD'].count()

# print(chart_data)
st.bar_chart(chart_data,  x="OPERATION_ID", y=['QUANTITY_SOLD'])
