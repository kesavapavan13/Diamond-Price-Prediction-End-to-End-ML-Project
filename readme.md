# 💎 Diamond Price Prediction – End-to-End Machine Learning Project

An end-to-end Machine Learning application that predicts the **price of a diamond** based on its physical dimensions and quality attributes.  
This project demonstrates the complete workflow from **data preprocessing → model training → model serialization → Streamlit deployment**.

---

# 🚀 Project Overview

This project was built to showcase a real-world Machine Learning deployment pipeline.

✔ Data preprocessing and feature engineering  
✔ Training a regression model using KNN  
✔ Saving the trained model with Pickle  
✔ Building an interactive UI with Streamlit  
✔ Real-time diamond price prediction  

The application allows users to input diamond characteristics and instantly receive an estimated price.

---

# 🧠 Problem Statement

Diamond pricing depends on multiple attributes such as:

- Carat weight
- Cut quality
- Color grade
- Clarity level
- Physical dimensions

The goal of this project is to build a Machine Learning model that can learn patterns from historical diamond data and predict the price accurately.

---

# 📊 Dataset Information

The dataset contains diamond characteristics including:

| Feature | Description |
|---|---|
| carat | Weight of the diamond |
| depth | Total depth percentage |
| table | Width of top relative to widest point |
| x | Length in mm |
| y | Width in mm |
| z | Depth in mm |
| cut | Quality of cut |
| color | Diamond color grading |
| clarity | Measurement of clarity |
| price | Target variable |

---

# 📂 Project Structure

```
diamond-price-prediction/
│
├── app.py
├── diamonds.csv
├── diamond_model.pkl
├── end_to_end_streamlit_deployment_using_knn.ipynb
├── requirements.txt
└── README.md
```


---

# 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle

---

# 🤖 Machine Learning Model

- Model Type: Regression
- Algorithm Used: K-Nearest Neighbors (KNN)
- Target Variable: `price`

### Model Pipeline
1. Load dataset
2. Perform preprocessing
3. Encode categorical features
4. Train KNN model
5. Save model as `.pkl`
6. Load model in Streamlit app

---

# 🔤 Feature Encoding

Categorical features are encoded using mapping dictionaries:

## Cut Encoding

Fair = 0
Good = 1
Very Good = 2
Premium = 3
Ideal = 4


## Color Encoding

J = 0
I = 1
H = 2
G = 3
F = 4
E = 5
D = 6


## Clarity Encoding

I1 = 0
SI2 = 1
SI1 = 2
VS2 = 3
VS1 = 4
VVS2 = 5
VVS1 = 6
IF = 7


---

# 🖥️ Streamlit Application

The Streamlit interface provides:

- Numeric inputs for diamond dimensions
- Dropdown menus for categorical attributes
- Predict button for price estimation
- Real-time prediction output

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

``` bash
git clone https://github.com/kesavapavan13/Diamond-Price-Prediction-End-to-End-ML-Project.git
cd diamond-price-prediction
```

## 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

```

## 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt

```

## 4️⃣ Run the Streamlit App
``` bash
streamlit run app.py
```
---

## 📌 Key Learnings

- End-to-end ML workflow

- Feature encoding consistency

- Model serialization with pickle

- Real-time deployment using Streamlit

- Practical ML application development

## 🔮 Future Improvements

- Add feature scaling pipeline

- Improve model accuracy with advanced algorithms

- Add input validation and data range checks

- Deploy on cloud (AWS / Streamlit Cloud)

- Use ColumnTransformer & Pipeline for robustness

## 👤 Author

Kesavapavan Gadde
 Aspiring Machine Learning Engineer | Data Science Enthusiast
