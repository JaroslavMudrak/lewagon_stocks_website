import streamlit as st
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

'''
## How amazing is this? Very much, indeed.
'''


##########  Get predictions ############################


url_predict = 'https://stocks-4dlywuyz2q-ew.a.run.app/predict?n=697'

response = requests.get(url_predict, verify=False)


#Get data from API
if response.status_code == 200:
    data = response.json()  # Assuming the API returns JSON data
else:
    st.error(f"Error: Unable to fetch data from API. Status code: {response.status_code}")


#Format the data into useful dataframe:
df_pred = pd.DataFrame(data)
df_pred = df_pred.rename(columns={'Close':'Prediction'})
# df_pred = df_pred.reset_index()
# df_pred = df_pred.rename(columns={'index':'Date'})
# df_pred['Date']= pd.to_datetime(df_pred['Date'])


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


# df_actuals['Date']= pd.to_datetime(df_actuals['Date'])


################ Merge data together ####################

final_df = pd.concat([df_actuals, df_pred], axis=1)
# final_df = final_df.reset_index()
# final_df = final_df.rename(columns={'index':'Date'})



#########################################################

# VISUALS

#Show table
# st.write(df_actuals)
# st.write(final_df)

#create chart:
sns.lineplot(data=final_df)



# #display chart using st.pyplot
st.pyplot(plt.gcf())
