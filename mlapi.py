# Libraries
from fastapi import FastAPI
import pickle
import numpy as np 
import requests 
import gdown

# Custom Files 
from customData import *
from encoding import *

# Initializing the app
app = FastAPI()
# Old plan path = "ml_files/model.pkl"
#https://drive.google.com/file/d/11qM7bVXQHrXQq-xFXSi7wcKlgU3kmyJb/view?usp=sharing
url = "https://drive.google.com/uc?id=11qM7bVXQHrXQq-xFXSi7wcKlgU3kmyJb"
output = "ml_files/output.pkl"
gdown.download(url, output, quiet=False)

with open("ml_files/output.pkl", "rb") as f:
    model = pickle.load(f)


def pipeline(item: InputData) -> EncodedData:
    # return {
    #     "Year" : [item.Year],
    #     "Trimester"  : [item.Trimester],
    #     "District" : [dist_encoding[item.District]], 
    #     "Neighbourhood" : [neigh_encoding[item.Neighbourhood]],
    #     "Average _rent" : [rent_encoding[item.Average_rent]]
    #     }
    return np.array([
                    item.Year, \
                    item.Trimester, \
                    dist_encoding[item.District], \
                    neigh_encoding[item.Neighbourhood], \
                    rent_encoding[item.Average_rent]
                    ])

@app.get('/')
async def scoring_endpoint(item : InputData):
    newData = pipeline(item)
    newData = newData.reshape((1, -1))
    yhat = model.predict(newData)[0]
    yhat = round(yhat, 2)
    pred_text = '€ ' + str(yhat)
    return {'prediction' : pred_text}

