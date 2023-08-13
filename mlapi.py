# Libraries
from fastapi import FastAPI
import pickle
import numpy as np 

# Custom Files 
from customData import *
from encoding import *

# Initializing the app
app = FastAPI()
with open("ml_files/model.pkl", "rb") as f:
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

