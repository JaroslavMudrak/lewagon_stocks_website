import streamlit as st
import requests

'''
## How amazing is this? Very much, indeed.
'''

url = 'https://stocks-4dlywuyz2q-ew.a.run.app/predict?n=2'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Assuming the API returns JSON data
    st.write('Fetching succesfull')
else:
    st.error(f"Error: Unable to fetch data from API. Status code: {response.status_code}")

data

st.write('Type of respnse')
type(response)

st.write('Type of data')
type(data)
