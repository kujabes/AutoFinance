import pandas as pd
import streamlit as st
import plotly.express as px
import json
import os

st.set_page_config(page_title='AutoFinance', page_icon='💲', layout='wide')

def load_transactions(file):
    '''
    Helper function to handle improper loading of transactions csv file
    Args:
        file - csv file containing transaction data
    Returns:
        df (pd.DataFrame) - loaded csv file
    '''
    try:
        # Reading in csv file and normalizing dataframe
        df = pd.read_csv(file)
        df.columns = [col.strip() for col in df.columns]
        df['Amount'] = df['Amount'].str.replace(',', '').astype(float)
        # %d - day, %b - month, %Y - Year
        df['Date'] = pd.to_datetime(df['Date'], format='%d %b %Y')
        return df
    except Exception as e:
        st.error(f'Error processing file: {str(e)}')
        return None

def main():
    st.title('Simple Finance Dashboard')

    uploaded_file = st.file_uploader('Upload your transaction csv file', type=['csv'])  

    if uploaded_file is not None:
        df = load_transactions(uploaded_file)

        if df is not None:
            debits_df = df[df["Debit/Credit"] == 'Debit'].copy()
            credits_df = df[df["Debit/Credit"] == 'Credit'].copy()

            tab1, tab2 = st.tabs(['Expenses (Debits)', 'Payments (Credits)'])
            with tab1:
                st.write(debits_df)

            with tab2:
                st.write(credits_df)

if __name__ == '__main__':
    main()
