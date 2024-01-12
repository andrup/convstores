import streamlit as st
import pandas as pd
import sys
import path

dir = path.Path(__file__).abspath()
sys.path.append(dir.parent)
st.write(dir)
st.write(dir.parent)
st.write(dir.parent.parent)

# try abosulute path  st.title(abspath)

dataset_path = dir.parent.parent.'/transactions.csv'
df = pd.read_csv(dataset_path)
st.title('Sales per PRODUCT_CATEGORY')

chart_data = df.groupby('PRODUCT_CATEGORY', as_index=False)['QUANTITY_SOLD'].count()

# print(chart_data)
st.bar_chart(chart_data,  x="PRODUCT_CATEGORY", y=['QUANTITY_SOLD'])
