import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from models import get_FFT, get_actuals, get_exp_smoothing, get_prophet_basic, get_nbeats



################ Get data from APIs ####################
@st.cache_data
def get_all_date_cached():

    df_actuals = get_actuals()
    df_fft = get_FFT()
    df_exp = get_exp_smoothing()
    df_basic_prophet = get_prophet_basic()
    df_nbeats = get_nbeats()



    ################ Merge data together ####################

    final_df = pd.concat([df_actuals, df_fft], axis=1)
    final_df = pd.concat([final_df, df_exp], axis=1)
    final_df = pd.concat([final_df, df_basic_prophet], axis=1)
    final_df = pd.concat([final_df, df_nbeats], axis=1)

    final_df.index = pd.to_datetime(final_df.index)

    #### last price
    last_price = int(df_actuals.iloc[-1,0])

    return final_df, last_price


final_df, last_price = get_all_date_cached()




###################### Visuals ######################



################# 1. Sidebar ############################

st.sidebar.markdown(f'## Current Apple stock price:  {last_price}')




st.sidebar.markdown(f"""
    ## Predict price:
    """)

option = st.sidebar.slider('Select a horizon:', 1, 365, 180)

horizon = len(get_actuals()) + option
filtered_df = final_df.iloc[:horizon]
# final_prices = filtered_df.iloc[-1].iloc[1:].rename(f'Predictions in {option} days').astype(int)
final_prices = filtered_df.iloc[-1].iloc[1:].rename(f'Prediction by model:').astype(int)



#Numeric predictions:

st.sidebar.markdown(f' ## Prediction in {option} days: {int(final_prices.mean())}')
st.sidebar.write(final_prices)



################# 2. Main board ############################


'''## Apple stock price ($)'''
# Chart
sns.lineplot(data=filtered_df)
st.pyplot(plt.gcf())





# ##########  Get predictions ############################

# ### 1. FFT
# url_fft = 'https://stocks-4dlywuyz2q-ew.a.run.app/fft?n=365'

# response = requests.get(url_fft, verify=False)


# #Get data from API
# if response.status_code == 200:
#     data = response.json()  # Assuming the API returns JSON data
# else:
#     st.error(f"Error: Unable to fetch data from API. Status code: {response.status_code}")


# #Format the data into useful dataframe:
# df_fft = pd.DataFrame(data)
# df_fft = df_fft.rename(columns={'Close':'FFT'})


# ### 2. Exponential Smoothing
# url_exp_sm = 'https://stocks-4dlywuyz2q-ew.a.run.app/exp_sm?n=365'

# response = requests.get(url_exp_sm, verify=False)


# #Get data from API
# if response.status_code == 200:
#     data = response.json()  # Assuming the API returns JSON data
# else:
#     st.error(f"Error: Unable to fetch data from API. Status code: {response.status_code}")


# #Format the data into useful dataframe:
# df_exp = pd.DataFrame(data)
# df_exp = df_exp.rename(columns={'Close':'Exp Smoothing'})

# last_date = df_exp.index.min()



# ### 3. Prophet basic
# url_exp_sm = 'https://stocks-4dlywuyz2q-ew.a.run.app/prophet_basic'

# response = requests.get(url_exp_sm, verify=False)


# #Get data from API
# if response.status_code == 200:
#     data = response.json()  # Assuming the API returns JSON data
# else:
#     st.error(f"Error: Unable to fetch data from API. Status code: {response.status_code}")


# #Format the data into useful dataframe:
# df_basic_prophet = pd.DataFrame(data)
# df_basic_prophet = df_basic_prophet.rename(columns={'ds':'Date', 'yhat':'Prophet basic'})
# df_basic_prophet = df_basic_prophet[df_basic_prophet['Date'] >= last_date]
# df_basic_prophet = df_basic_prophet.set_index('Date')


#########################################################


################ Get Actuals ############################

# url_actuals = 'https://stocks-4dlywuyz2q-ew.a.run.app/actuals'
# response_actuals = requests.get(url_actuals, verify=False)

# #Get data from API
# if response.status_code == 200:
#     data_actuals = response_actuals.json()  # Assuming the API returns JSON data
# else:
#     st.error(f"Error: Unable to fetch data from API. Status code: {response.status_code}")

# #########################################################

# #Format the data into useful dataframe:
# df_actuals = pd.DataFrame(data_actuals)
# df_actuals = df_actuals.rename(columns={'Close':'Actuals'})
