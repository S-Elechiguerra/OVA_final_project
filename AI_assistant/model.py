import pickle

# Function to load the pre-trained model
def load_model():
    with open('model/logistic_regression_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model