import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    data = pd.read_csv("breast_cancer_data.csv")
    data['Date'] = pd.to_datetime(data['Date'])
    return data

def get_summary(data):
    summary = pd.DataFrame({
        'radius': [radius_input.value],
        'texture': [texture_input.value],
        'perimeter': [perimeter_input.value],
        'area': [area_input.value],
        'smoothness': [smoothness_input.value],
        'compactness': [compactness_input.value],
        'concavity': [concavity_input.value],
        'concave points': [concave_points_input.value],
        'symmetry': [symmetry_input.value],
        'fractal_dimension': [fractal_dimension_input.value]
    })
    return summary

# Function to calculate mean, se, and worst
def classify_features(inputs):
    classified_inputs = {}
    for key, value in inputs.items():
        classified_inputs[f'{key}_mean'] = value
        classified_inputs[f'{key}_se'] = value * 0.1  # Simulated logic for SE
        classified_inputs[f'{key}_worst'] = value * 1.5  # Simulated logic for worst
    return classified_inputs

# User inputs
import ipywidgets as widgets
from IPython.display import display

# Create text boxes for each input feature
radius_input = widgets.FloatText(
    value=0.0,
    description='Radius:',
    disabled=False
)

texture_input = widgets.FloatText(
    value=0.0,
    description='Texture:',
    disabled=False
)

perimeter_input = widgets.FloatText(
    value=0.0,
    description='Perimeter:',
    disabled=False
)

area_input = widgets.FloatText(
    value=0.0,
    description='Area:',
    disabled=False
)

smoothness_input = widgets.FloatText(
    value=0.0,
    description='Smoothness:',
    disabled=False
)

compactness_input = widgets.FloatText(
    value=0.0,
    description='Compactness:',
    disabled=False
)

concavity_input = widgets.FloatText(
    value=0.0,
    description='Concavity:',
    disabled=False
)

concave_points_input = widgets.FloatText(
    value=0.0,
    description='Concave Points:',
    disabled=False
)

symmetry_input = widgets.FloatText(
    value=0.0,
    description='Symmetry:',
    disabled=False
)

fractal_dimension_input = widgets.FloatText(
    value=0.0,
    description='Fractal Dimension:',
    disabled=False
)

# Display all the inputs
display(radius_input, texture_input, perimeter_input, area_input, 
        smoothness_input, compactness_input, concavity_input, 
        concave_points_input, symmetry_input, fractal_dimension_input)

# Function to collect user input from the widgets and classify them
def collect_user_inputs():
    user_inputs = {
        'radius': radius_input.value,
        'texture': texture_input.value,
        'perimeter': perimeter_input.value,
        'area': area_input.value,
        'smoothness': smoothness_input.value,
        'compactness': compactness_input.value,
        'concavity': concavity_input.value,
        'concave points': concave_points_input.value,
        'symmetry': symmetry_input.value,
        'fractal_dimension': fractal_dimension_input.value
    }
    return user_inputs

# Run the function to collect inputs
user_inputs = collect_user_inputs()
print(user_inputs)


# Classify inputs internally
classified_inputs = classify_features(user_inputs)

# Ensure the order of features matches what the model expects
feature_columns = [
    'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean',
    'compactness_mean', 'concavity_mean', 'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
    'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
    'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se', 'fractal_dimension_se',
    'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst', 'smoothness_worst',
    'compactness_worst', 'concavity_worst', 'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst'
]

features = [classified_inputs[feature] for feature in feature_columns]

# SVC Model with GridSearchCV
svc = SVC(probability=True)
parameters = {
    'gamma': [0.0001, 0.001, 0.01, 0.1],
    'C': [0.01, 0.05, 0.5, 0.1, 1, 10, 15, 20]
}
grid_search = GridSearchCV(svc, parameters)
grid_search.fit(X_train, y_train)
model = grid_search.best_estimator_

# Define the prediction function
def predict(model, features):
    prediction = model.predict([features])
    return prediction[0]

# Make a prediction
prediction = predict(model, features)
if prediction == 1:
    print("Predicted: Malign - Cancerous")
else:
    print("Predicted: Benign - Non Cancerous")

# Health recommendations based on prediction
if prediction == 1:
    print("Here are some additional recommendations for your patients:")
    print("- **Give them the facts about their cancer diagnosis:** Inform the exact type of cancer they have and how advanced it is. Where the cancer is located and whether it is considered rare or common, fast- or slow-growing. The answers to these questions will help them make informed decisions about the treatment.")
    print("- **Explore their treatment options:** Let them know which ones might work best for them. Explain the side effects they can expect from each treatment option and how they could affect their lifestyle.")
    print("- **Looking after quality of life:** Successful care requires close collaboration and open communication about your patient concerns and what they are feeling. Talk about pain. Let them know that certain sorts of pain may be warning signs of serious problems that may need urgent attention like:Back pain which suddenly becomes much worse. Pain in the hips or legs which becomes very severe when standing or walking. Persistent headaches. Severe stomach pain and diarrhea after chemotherapy. Severe pain from mouth ulcers that makes it difficult to eat or drink.")
else:
    print("Here are some health tips for general wellness:")
    print("- **Smoking & Tobacco:** Tobacco use is accountable for at least 30% of all cancer deaths, and smoking causes nearly 90% of all lung cancers. People who live with smokers are more likely to develop lung cancer and even limited exposure to secondhand smoke can raise your heart disease risk.")
    print("- **Stay Active:** Our body runs on food. Foods affect how we feel, how it operates and the risk for diseases like cancer.Reduce intake of red and processed meats by choosing fish, seafood or poultry.Increase the amount of fruits and vegetables you eat.Consuming alcohol in any quantity has been shown to increase the risk of cancers.Choose whole grains or other whole food carbohydrates rather than processed carbohydrates.")    
    print("- **Regular Check-ups:** Preventive healthcare is important, be an active advocate of regular screening test. If your patient is taking, or have been told to take, hormone replacement therapy or oral contraceptives (birth control pills),explain them the risks.Here are some of the most important recommendations you can give to your patients: Maintaining a healthy body weight and tell them how it lowers the risk for more than 10 types of cancer.Being physically can help maintain a healthy weight.The best way to protect from skin cancer is to limit the exposure to UV rays from the sun and tanning beds.The HPV vaccine is the best protection against HPV and related cancers. All boys and girls between the ages of 11 and 12 should complete the HPV vaccine series.Hepatitis B and C can cause long-term illness that leads to liver damage and liver cancer. Hepatitis C also can cause non-Hodgkin lymphoma.")
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

# Title of the app
st.title('Welcome to OVA Breast Cancer Predictor App')

# Load data - Placeholder function
def load_data():
    df = pd.read_csv('breast_cancer_data.csv')
    df = pd.DataFrame()
    return df

# Function to calculate mean, se, and worst
def classify_features(inputs):
    classified_inputs = {}
    for key, value in inputs.items():
        classified_inputs[f'{key}_mean'] = value
        classified_inputs[f'{key}_se'] = value * 0.1  # Simulated logic for SE
        classified_inputs[f'{key}_worst'] = value * 1.5  # Simulated logic for worst
    return classified_inputs

# User input function
def get_user_inputs():
    radius = st.sidebar.number_input('Radius:', 0.0, 100.0, step=0.1)
    texture = st.sidebar.number_input('Texture:', 0.0, 100.0, step=0.1)
    perimeter = st.sidebar.number_input('Perimeter:', 0.0, 100.0, step=0.1)
    area = st.sidebar.number_input('Area:', 0.0, 5000.0, step=1.0)
    smoothness = st.sidebar.number_input('Smoothness:', 0.0, 1.0, step=0.001)
    compactness = st.sidebar.number_input('Compactness:', 0.0, 1.0, step=0.001)
    concavity = st.sidebar.number_input('Concavity:', 0.0, 1.0, step=0.001)
    concave_points = st.sidebar.number_input('Concave Points:', 0.0, 1.0, step=0.001)
    symmetry = st.sidebar.number_input('Symmetry:', 0.0, 1.0, step=0.001)
    fractal_dimension = st.sidebar.number_input('Fractal Dimension:', 0.0, 1.0, step=0.001)

    user_inputs = {
        'radius': radius,
        'texture': texture,
        'perimeter': perimeter,
        'area': area,
        'smoothness': smoothness,
        'compactness': compactness,
        'concavity': concavity,
        'concave points': concave_points,
        'symmetry': symmetry,
        'fractal_dimension': fractal_dimension
    }
    return user_inputs

# Main function for Streamlit app
def main():
    # Load data
    data = load_data()
    
    # Get user inputs
    user_inputs = get_user_inputs()
    
    # Classify inputs
    classified_inputs = classify_features(user_inputs)
    
    # Ensure the order of features matches what the model expects
    feature_columns = [
        'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean',
        'compactness_mean', 'concavity_mean', 'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
        'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
        'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se', 'fractal_dimension_se',
        'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst', 'smoothness_worst',
        'compactness_worst', 'concavity_worst', 'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst'
    ]
    features = [classified_inputs[feature] for feature in feature_columns]

    #