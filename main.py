import pandas as pd
import streamlit as st

def get_bad_items(mid):

    df_market = dataset_df[dataset_df['UNIQUE_MARKET_ID'] == mid]
    df = df_market.groupby('PRODUCT_NAME')['QUANTITY_SOLD'].sum().reset_index()
    filtered_df = df[df['QUANTITY_SOLD'] <= 1]
    return filtered_df['PRODUCT_NAME'].tolist()

def get_recommended_items(qty):
    df = dataset_df.groupby('PRODUCT_NAME')['QUANTITY_SOLD'].sum().reset_index()
    filtered_df = df.sort_values(by='QUANTITY_SOLD', ascending=False)
    return filtered_df.head(qty)['PRODUCT_NAME'].tolist()

def check_if_item_in_market(mid, rec_items_list):
    df_market = dataset_df[dataset_df['UNIQUE_MARKET_ID'] == mid]
    new_list = []
    for product in rec_items_list:
        if product not in df_market['PRODUCT_NAME'].values:
            new_list.append(product)
    return new_list

dataset_path ='transactions.csv'
dataset_df = pd.read_csv(dataset_path)
st.title('Optimization of Markets')
st.write('Enter a market_id for recommendations (e.g.315344 , 278594 ): ')
mid = st.number_input("Market ID Value", value=315344)

rec_items_list = get_recommended_items(10)
print(f'recommended {rec_items_list}')

print(f'Recommendation for Market_Id: {mid} ')

bad_items_list = get_bad_items(mid)
print(f'remove {bad_items_list}')
st.write('remove: ', bad_items_list)

new_items_list = check_if_item_in_market(mid, rec_items_list)
print(f'added {new_items_list}')
st.write('added: ', new_items_list)
