import pandas as pd
import requests
import streamlit as st

def get_actuals():
    url_actuals = 'https://stocks-4dlywuyz2q-ew.a.run.app/actuals'
    response_actuals = requests.get(url_actuals, verify=False)

    #Get data from API
    if response_actuals.status_code == 200:
        data_actuals = response_actuals.json()  # Assuming the API returns JSON data
    else:
        st.error(f"Error: Unable to fetch data from API. Status code: {response_actuals.status_code}")

    #########################################################

    #Format the data into useful dataframe:
    df_actuals = pd.DataFrame(data_actuals)
    df_actuals = df_actuals.rename(columns={'Close':'Actuals'})

    return df_actuals


last_date = get_actuals().index.max()

def get_FFT():
    url_fft = 'https://stocks-4dlywuyz2q-ew.a.run.app/fft?n=365'

    response = requests.get(url_fft, verify=False)


    #Get data from API
    if response.status_code == 200:
        data = response.json()  # Assuming the API returns JSON data
    else:
        st.error(f"Error: Unable to fetch data from API. Status code: {response.status_code}")


    #Format the data into useful dataframe:
    df_fft = pd.DataFrame(data)
    df_fft = df_fft.rename(columns={'Close':'FFT'})

    return df_fft




def get_exp_smoothing():
    ### 2. Exponential Smoothing
    url_exp_sm = 'https://stocks-4dlywuyz2q-ew.a.run.app/exp_sm?n=365'

    response = requests.get(url_exp_sm, verify=False)


    #Get data from API
    if response.status_code == 200:
        data = response.json()  # Assuming the API returns JSON data
    else:
        st.error(f"Error: Unable to fetch data from API. Status code: {response.status_code}")


    #Format the data into useful dataframe:
    df_exp = pd.DataFrame(data)
    df_exp = df_exp.rename(columns={'Close':'Exp Smoothing'})

    return df_exp


def get_prophet_basic():
    ### 3. Prophet basic
    url_exp_sm = 'https://stocks-4dlywuyz2q-ew.a.run.app/prophet_basic'

    response = requests.get(url_exp_sm, verify=False)


    #Get data from API
    if response.status_code == 200:
        data = response.json()  # Assuming the API returns JSON data
    else:
        st.error(f"Error: Unable to fetch data from API. Status code: {response.status_code}")


    #Format the data into useful dataframe:
    df_basic_prophet = pd.DataFrame(data)
    df_basic_prophet = df_basic_prophet.rename(columns={'ds':'Date', 'yhat':'Prophet basic'})
    df_basic_prophet = df_basic_prophet[df_basic_prophet['Date'] >= last_date]
    df_basic_prophet = df_basic_prophet.set_index('Date')

    return df_basic_prophet
