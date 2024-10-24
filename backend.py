import pandas as pd
import matplotlib.pyplot as plt

@st.cache
def load_data():
    data = pd.read_csv("breast_cancer_data.csv")
    return data

def load_model():
    with open('logistic_regression_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model