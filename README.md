# BarcelonaRent-Predictor
Elevate your Barcelona rental experience with this project: a fusion of AI and user-friendly design, offering 98% accurate 
price predictions through a FastAPI-powered ML model and an engaging Streamlit frontend. Make smarter real estate choices today.
- #### <a href = "https://barcelona-rent-predictor.onrender.com"> barcelona-rent-predictor API </a>
- #### <a href = "https://www.kaggle.com/code/gracehephzibahm/prediction-of-rent-prices-in-barcelona"> Kaggle Notebook </a>

# Objective 
Embark on a journey to redefine how Barcelona's rental market is understood and navigated. The objective is to develop a comprehensive and accurate 
prediction solution that empowers property owners, tenants, and real estate enthusiasts with insights to make confident decisions. Through 
the synergy of advanced machine learning, streamlined API accessibility, and an interactive web-page, the goal is to achieve a new standard of 0.98 
R-squared accuracy, illuminating the path to informed choices and optimal rental pricing. Here is the future of Barcelona's real estate 
landscape with data-driven innovation.

# Skills
- **Frontend:** Streamlit
- **API:** FastAPI, Postman, Requests, Pydantic
- **API Hosting:** Uvicorn, Gunicorn, Render
- **ML Model:** Scikit-Learn, Pickle, Numpy
- **Data Visualization:** Matplotlib, Seaborn
- **Data Handling:** Pandas

# Repository Details
## API
These files were used for hosting on render. 
```
API
  |---- CustomData.py
  |---- encoding.py
  |---- mlapi.py
  |---- requirements.txt
```
**NOTE:**
After trying to host on multiple platforms, <a href = "https://render.com/">Render</a> finally worked. 
Others failed to work because of constraints.
A Few of the common issues that arise while hosting on Render are

- Version of Scikit Learn on Render is only up to 1.0.2. Therefore it created a problem when my pickled version was from Scikit-Learn version 1.3.0
- In local hosting I used ```uvicorn mlapi:app --reload```. But in render hosting, the start command was ```uvicorn mlapi:app --host 0.0.0.0 --port $PORT```

## Streamlit 
These files are used for hosting. 
```
Streamlit
  |---- app.py
  |---- encoding.py
```

## ML Model 
I use MiniConda and Jupyter Notebook to develop ML Models. These files are used for creating the ml model.
```
ML Model
 |---- ml_files
          |---- data.csv
          |---- notebook.ipynb
```
# For More Details 
- To set up locally -> Refer ```installation.md```
- For API Instructions -> Refer ```api_instructions.md```

# Developed By Grace Hephzibah ✨
