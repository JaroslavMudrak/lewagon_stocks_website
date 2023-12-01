import streamlit as st
import requests

'''
# How amazing is this? Very much, indeed.
'''

url = 'https://stocks-4dlywuyz2q-ew.a.run.app/predict?n=2'

response = requests.get(url)
response
