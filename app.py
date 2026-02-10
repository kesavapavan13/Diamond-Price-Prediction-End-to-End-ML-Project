import streamlit as st
import pandas as pd
import pickle

# Load model
with open("diamond_model.pkl", "rb") as file:
    loaded_model = pickle.load(file)

st.title("Diamond price Prediction")

# ---- NUMERICAL INPUTS ----
carat = st.number_input("carat", min_value=0, value=7)
depth = st.number_input("depth", min_value=0, value=100)
table = st.number_input("table", min_value=0, value=100)
x = st.number_input("x", min_value = 0, value=50)
y = st.number_input("y", min_value = 0, value=50)
z = st.number_input("z", min_value = 0, value=50)

# ---- CATEGORICAL INPUTS ----
# ---- CATEGORICAL MAPS ----
cut_map = {
    'Fair': 0,
    'Good': 1,
    'Very Good': 2,
    'Premium': 3,
    'Ideal': 4
}

color_map = {
    'J': 0,
    'I': 1,
    'H': 2,
    'G': 3,
    'F': 4,
    'E': 5,
    'D': 6
}

clarity_map = {
    'I1': 0,
    'SI2': 1,
    'SI1': 2,
    'VS2': 3,
    'VS1': 4,
    'VVS2': 5,
    'VVS1': 6,
    'IF': 7
}

# ---- STREAMLIT INPUTS (FIRST!) ----
cut = st.selectbox("cut", ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
color = st.selectbox("color", ['J', 'I', 'H', 'G', 'F', 'E', 'D'])
clarity = st.selectbox("clarity", ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])

# ---- ENCODE INPUTS ----
cut_encoded = cut_map[cut]
color_encoded = color_map[color]
clarity_encoded = clarity_map[clarity]

# ---- CREATE NUMERIC INPUT DATAFRAME (MATCH TRAINING ORDER) ----
input_data = pd.DataFrame({
    "carat": [carat],
    "depth": [depth],
    "table": [table],
    "x": [x],
    "y": [y],
    "z": [z],
    "cut": [cut_encoded],
    "color": [color_encoded],
    "clarity": [clarity_encoded]
})


# ---- PREDICTION ----
if st.button("predict diamond price"):
    prediction = loaded_model.predict(input_data)
    st.success(f'estimated diamond price: $ {prediction[0]:.2f}')

