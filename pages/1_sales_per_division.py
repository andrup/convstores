import streamlit as st
import pandas as pd
import sys
import path

dir = path.Path(__file__).abspath()

dataset_path = dir.parent.parent + '/transactions.csv'
df = pd.read_csv(dataset_path)
st.title('Sales per Division')

chart_data = df.groupby('DIVISION', as_index=False)['QUANTITY_SOLD'].count()

st.bar_chart(chart_data,  x="DIVISION", y=['QUANTITY_SOLD'])
