import streamlit as st
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

'''
## How amazing is this? Very much, indeed.
'''


##########  Get predictions ############################

### 1. FFT
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


#########################################################


################ Get Actuals ############################

url_actuals = 'https://stocks-4dlywuyz2q-ew.a.run.app/actuals'
response_actuals = requests.get(url_actuals, verify=False)

#Get data from API
if response.status_code == 200:
    data_actuals = response_actuals.json()  # Assuming the API returns JSON data
else:
    st.error(f"Error: Unable to fetch data from API. Status code: {response.status_code}")

#########################################################

#Format the data into useful dataframe:
df_actuals = pd.DataFrame(data_actuals)
df_actuals = df_actuals.rename(columns={'Close':'Actuals'})





################ Merge data together ####################

final_df = pd.concat([df_actuals, df_fft], axis=1)
final_df = pd.concat([final_df, df_exp], axis=1)



#########################################################

# VISUALS




#create chart:
sns.lineplot(data=final_df)

#Show table
# st.write(df_actuals)
st.write(final_df)



# #display chart using st.pyplot
st.pyplot(plt.gcf())
