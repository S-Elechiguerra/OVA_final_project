from flask import Blueprint, jsonify, request
from .model import load_model

# Blueprint for the API routes
predict_bp = Blueprint('predict_bp', __name__)

# Load the model when the Flask app starts
model = load_model()

# Classify features for input
def classify_features(inputs):
    classified_inputs = {}
    for key, value in inputs.items():
        classified_inputs[f'{key}_mean'] = value
        classified_inputs[f'{key}_se'] = value * 0.1  # Simulated logic for SE
        classified_inputs[f'{key}_worst'] = value * 1.5  # Simulated logic for worst
    return classified_inputs

# The list of expected feature columns (for correct input order)
feature_columns = [
    'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean',
    'compactness_mean', 'concavity_mean', 'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
    'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
    'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se', 'fractal_dimension_se',
    'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst', 'smoothness_worst',
    'compactness_worst', 'concavity_worst', 'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst'
]

# Define the prediction route
@predict_bp.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse the JSON payload from the request
        data = request.json

        # Validate input data
        required_fields = ['radius', 'texture', 'perimeter', 'area', 'smoothness', 'compactness', 
                           'concavity', 'concave_points', 'symmetry', 'fractal_dimension']
        for field in required_fields:
            if field not in data or not isinstance(data[field], (int, float)):
                return jsonify({'error': f'Missing or invalid value for {field}'}), 400
        
        # Collect user inputs from the request
        user_inputs = {field: data[field] for field in required_fields}

        # Classify inputs using the custom function
        classified_inputs = classify_features(user_inputs)

        # Prepare the feature array in the correct order
        features = [classified_inputs[feature] for feature in feature_columns]

        # Make a prediction using the logistic regression model
        prediction = model.predict([features])

        # Return the prediction as JSON
        result = {
            'prediction': 'Malign - Cancerous' if prediction[0] == 1 else 'Benign - Non Cancerous',
            'recommendations': []
        }

        # Add health recommendations based on the prediction
        if prediction[0] == 1:
            result['recommendations'] = [
                "Give them the facts about their cancer diagnosis: Inform the exact type of cancer they have and how advanced it is.",
                "Explore their treatment options: Let them know which treatments might work best for them.",
                "Looking after quality of life: Talk about their concerns, pain management, and other symptoms."
            ]
        else:
            result['recommendations'] = [
                "Avoid smoking and secondhand smoke exposure.",
                "Stay active and eat healthy to reduce cancer risk.",
                "Schedule regular check-ups and cancer screenings."
            ]

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500
