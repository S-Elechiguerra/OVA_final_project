import streamlit as st
import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

# Title
st.title('Welcome to OVA Breast Cancer Predictor App')

# Function to calculate mean, SE, and worst
def classify_features(inputs):
    classified_inputs = {}
    for key, value in inputs.items():
        classified_inputs[f'{key}_mean'] = value
        classified_inputs[f'{key}_se'] = value * 0.1  # Simulated logic for SE
        classified_inputs[f'{key}_worst'] = value * 1.5  # Simulated logic for worst
    return classified_inputs

# Sidebar Inputs
st.sidebar.header('Input Features')
radius = st.sidebar.number_input('Radius')
texture = st.sidebar.number_input('Texture')
perimeter = st.sidebar.number_input('Perimeter')
area = st.sidebar.number_input('Area')
smoothness = st.sidebar.number_input('Smoothness')
compactness = st.sidebar.number_input('Compactness')
concavity = st.sidebar.number_input('Concavity')
concave_points = st.sidebar.number_input('Concave Points')
symmetry = st.sidebar.number_input('Symmetry')
fractal_dimension = st.sidebar.number_input('Fractal Dimension')

# Collect User Inputs
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

# Initialize the SVC model with GridSearchCV
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
if st.sidebar.button('Predict'):
    prediction = predict(model, features)
    if prediction == 1:
        st.write("Predicted: Malign - Cancerous")
        st.write("Here are some additional recommendations for your patients:")
        st.write("- **Give them the facts about their cancer diagnosis:** Inform the exact type of cancer they have and how advanced it is. Where the cancer is located and whether it’s considered rare or common, fast- or slow-growing. The answers to these questions will help them make informed decisions about the treatment.")
        st.write("- **Explore their treatment options:** Let them know which ones might work best for them. Explain the side effects they can expect from each treatment option and how they could affect their lifestyle.")
        st.write("- **Looking after quality of life:** Successful care requires close collaboration and open communication about your patient concerns and what they are feeling. Talk about pain. Let them know that certain sorts of pain may be warning signs of serious problems that may need urgent attention like: Back pain which suddenly becomes much worse. Pain in the hips or legs which becomes very severe when standing or walking. Persistent headaches. Severe stomach pain and diarrhea after chemotherapy. Severe pain from mouth ulcers that makes it difficult to eat or drink.")
    else:
        st.write("Predicted: Benign - Non Cancerous")
        st.write("Here are some health tips for general wellness:")
        st.write("- **Smoking & Tobacco:** Tobacco use is accountable for at least 30% of all cancer deaths, and smoking causes nearly 90% of all lung cancers. People who live with smokers are more likely to develop lung cancer and even limited exposure to secondhand smoke can raise your heart disease risk.")
        st.write("- **Stay Active:** Our body runs on food. Foods affect how we feel, how it operates and the risk for diseases like cancer. Reduce intake of red and processed meats by choosing fish, seafood or poultry. Increase the amount of fruits and vegetables you eat. Consuming alcohol in any quantity has been shown to increase the risk of cancers. Choose whole grains or other whole food carbohydrates rather than processed carbohydrates.")
        st.write("- **Regular Check-ups:** Preventive healthcare is important, be an active advocate of regular screening tests. If your patient is taking, or has been told to take, hormone replacement therapy or oral contraceptives (birth control pills), explain the risks. Here are some of the most important recommendations you can give to your patients: Maintaining a healthy body weight lowers the risk for more than 10 types of cancer. Being physically active can help maintain a healthy weight. The best way to protect from skin cancer is to limit exposure to UV rays from the sun and tanning beds. The HPV vaccine is the best protection against HPV and related cancers. All boys and girls between the ages of 11 and 12 should complete the HPV vaccine series. Hepatitis B and C can cause long-term illness that leads to liver damage and liver cancer. Hepatitis C also can cause non-Hodgkin lymphoma.")
