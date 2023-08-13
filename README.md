# BarcelonaRent-Predictor
Elevate your Barcelona rental experience with this project: a fusion of AI and user-friendly design, offering 98% accurate 
price predictions through a FastAPI-powered ML model and an engaging Streamlit frontend. Make smarter real estate choices today.
- #### <a href = "https://barcelona-rent-predictor.onrender.com"> barcelona-rent-predictor API </a>
- #### <a href = "https://www.kaggle.com/code/gracehephzibahm/prediction-of-rent-prices-in-barcelona"> Kaggle Notebook </a>

# Objective 
Embark on a journey to redefine how Barcelona's rental market is understood and navigated. Our objective is to develop a comprehensive and accurate 
prediction solution that empowers property owners, tenants, and real estate enthusiasts with the insights needed to make confident decisions. Through 
the synergy of advanced machine learning, streamlined API accessibility, and an interactive frontend, our goal is to achieve a new standard of 0.98 
R-squared accuracy, illuminating the path to informed choices and optimal rental pricing. Join us in reshaping the future of Barcelona's real estate 
landscape with data-driven innovation.

# Skills
- **Frontend:** Streamlit
- **API:** FastAPI, Postman, requests, Pydantic
- **API Hosting:** uvicorn, gunicorn, render
- **ML Model:** Scikit-learn, pickle, numpy
- **Data Visualization:** Matplotlib
- **Data Handling:** Pandas

# Repository Details
## API
These files were used for hosting on render. 
```
API
  |---- CustomData.py
  |---- encoding.py
  |---- mlapi.py
  |---- api_requirements.txt
  |---- ml_files/model.pkl
  |---- ml_files/.gitattributes
```
**NOTE:**
After trying to host on multiple platforms, <a href = "https://render.com/">Render</a> finally worked. 
Others failed to work because of memory contraints.
Few common issues that rise while hosting on render are

- Version of Scikit Learn on Render is only upto 1.0.2. Therefore it created a problem when my pickled version was from scikit-learn version 1.3.0
- In local hosting I used ```uvicorn mlapi:app --reload```. But in render hosting, the start command was ```uvicorn mlapi:app --host 0.0.0.0 --port $PORT```
- The build command is ```pip install -r api_requirements.txt```

## Streamlit 
These files are were used for hosting. 
```
Streamlit
  |---- app.py
  |---- encoding.py
```

## ML Model 
I use MiniConda and Jupyter Notebook to develop ML Model. These files are used for developing the ml model.
```
ML Model
 |---- ml_files
          |---- .gitattributes
          |---- data.csv
          |---- model.pkl
          |---- notebook.ipynb
```
# For More Details 
- To set up locally -> Refer ```installation.md```
- For API Instructions -> Refer ```api_instructions.md```

# Developed By Grace Hephzibah ✨
