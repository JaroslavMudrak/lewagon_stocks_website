import streamlit as st
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

'''
## How amazing is this? Very much, indeed.
'''

url = 'https://stocks-4dlywuyz2q-ew.a.run.app/predict?n=100'

response = requests.get(url, verify=False)


#Get data from API
if response.status_code == 200:
    data = response.json()  # Assuming the API returns JSON data
else:
    st.error(f"Error: Unable to fetch data from API. Status code: {response.status_code}")


#Format the data into useful dataframe:
data_df = pd.DataFrame(data)
data_df = data_df.reset_index()
data_df = data_df.rename(columns={'index':'Date'})
data_df['Date']= pd.to_datetime(data_df['Date'])

#Show table
# st.write(data_df)

#create chart:
sns.lineplot(x=data_df['Date'], y=data_df['Close'])

#display chart using st.pyplot
st.pyplot(plt.gcf())
