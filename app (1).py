
import streamlit as st
import pickle
import pandas as pd
import numpy as np

model_data = pickle.load(open('house_price_model.pkl', 'rb'))
model = model_data['model']
feature_columns = model_data['features']

st.title('House Price Predictor')
st.write('Enter home details below to get an estimated sale price')

overall_qual = st.slider('Overall Quality of Home', min_value=1, max_value=10, value=5)
gr_liv_area = st.number_input('Above Ground Living Area (sq ft)', min_value=300, max_value=6000, value=1500)
garage_cars = st.number_input('Garage Size (number of cars)', min_value=0, max_value=5, value=2)
total_bsmt_sf = st.number_input('Total Basement Area (sq ft)', min_value=0, max_value=3000, value=800)
year_built = st.number_input('Year Built', min_value=1870, max_value=2024, value=2000)

if st.button('Predict Price'):
    input_data = pd.DataFrame([np.zeros(len(feature_columns))], columns=feature_columns)
    
    input_data['OverallQual'] = overall_qual
    input_data['GrLivArea'] = gr_liv_area
    input_data['GarageCars'] = garage_cars
    input_data['TotalBsmtSF'] = total_bsmt_sf
    input_data['YearBuilt'] = year_built
    
    prediction = model.predict(input_data)
    st.success(f'Estimated House Price: ${prediction[0]:,.2f}')
#Write the streamlit app
