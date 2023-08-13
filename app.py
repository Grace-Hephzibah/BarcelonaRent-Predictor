# Libraries
import streamlit as st
import requests

# Custom Files
from encoding import *
from  customData import * 

URL = 'https://barcelona-rent-predictor.onrender.com'
#Local Host -> 'http://127.0.0.1:8000' # API hosted site 

# Header 
st.set_page_config(
    page_title="Barcelona Rents",
    page_icon="🪙",
    layout="wide"
)



# Intro 
st.markdown("<h1 style = 'text-align:center;'> Welcome to Barcelona Rents 🪙 </h1>", unsafe_allow_html=True)

st.write('''###### Explore My Code Here:  https://github.com/Grace-Hephzibah/BarcelonaRent-Predictor ''')
st.write('''###### Kaggle:  https://www.kaggle.com/code/gracehephzibahm/prediction-of-rent-prices-in-barcelona ''')

st.divider()



# Data required for prediction
a,b,c = st.columns(3)
with a:
    min_year = min(year_var)
    year = st.number_input('Year', min_value = min_year)
with b:
    min_trimester = min(trimester_var)
    max_trimester = max(trimester_var)
    trimester = st.number_input('Trimester',min_value = min_trimester, max_value = max_trimester)
with c:
    district = st.selectbox('District', dist_encoding.keys())

d,e = st.columns(2)
with d:
    neighbourhood = st.selectbox('Neighbourhood', neigh_encoding.keys())
with e:
    avg_rent = st.selectbox('Average Rent Type', rent_encoding.keys())


# Preparing the request Body 
request_body =     {
        "Year" : year,
        "Trimester"  : trimester,
        "District" : district, 
        "Neighbourhood" : neighbourhood,
        "Average_rent" : avg_rent
        }


status_submit = st.button("Submit")
st.divider()

# Answer section 
f, g, h = st.columns([1,2,4])
ans_val = 'Click Submit!'

with f: 
    st.write('<h3>Prediction : </h3>', unsafe_allow_html=True) 
with g:
    ans = st.empty()
    ans.code(ans_val)
with h:
    st.write(" ")

if status_submit:
    response = requests.get(URL, json = request_body).json()
    ans.code(response['prediction'])

st.divider()