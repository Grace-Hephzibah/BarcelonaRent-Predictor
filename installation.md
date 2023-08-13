# WorkFlow Plan
- Pushed only the api required files to the repo first and hosted it on render
- Then pushed the other files and hosted on streamlit

# Steps To Test Locally 
## Step 1: Clone The Repo
## Step 2: Install The Libraries 
- Visual Studio Code [Prefarabbly On Virtual Environment]
```pip install fastapi gunicorn numpy pandas pydantic scikit-learn streamlit uvicorn ```

- Mini Conda [Optional - Do this if you want to run the ml_files/notebook.ipynb]
```conda install matplotlib notebook numpy pandas scikit-learn==1.0.1 seaborn```
## Step 3: Locally Host API 
``` uvicorn mlapi:app --reload```
## step 4: Locally Host Streamlit 
``` streamlit run app.py```

# To test the API on Postman
**GET** ```http://127.0.0.1:8000```
Under BODY-> RAW set to JSON 
```
{
    "Year" : 2020, 
    "Trimester"  : 2, 
    "District" : "Sant Marti", 
    "Neighbourhood" : "la Verneda i la Pau", 
    "Average_rent" : "average rent per surface (euro/m2)" 
}
```
Your Output will be like
```
{
    'prediction' : '€ 704.93'
}
```
