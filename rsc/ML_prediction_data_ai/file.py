# Import necessary libraries
from pandas import read_csv
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
import joblib
import os

# Check if the trained model is already cached
model_cache_path = 'trained_model.joblib'

if os.path.exists(model_cache_path):
    # Load the cached model
    model_data = joblib.load(model_cache_path)
    model = model_data['model']
    scaler = model_data['scaler']
else:
    # Load CSV data
    data = read_csv('data3.csv')

    # Extract features (a, b, c) and target variable (outcome)
    X = data[['a', 'b', 'c']]
    y = data['outcome']

    # Standardize the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Create and train a deep learning model (Multi-layer Perceptron)
    model = MLPRegressor(hidden_layer_sizes=(100, 50), max_iter=1000, random_state=42)
    model.fit(X_scaled, y)

    # Cache the trained model
    model_data = {'model': model, 'scaler': scaler}
    joblib.dump(model_data, model_cache_path)

# Function to predict outcome based on input values a, b, c
def predict_outcome(a, b, c):
    input_data = scaler.transform([[a, b, c]])
    prediction = model.predict(input_data)
    return prediction[0]

# Prompt user for input
a = float(input("Enter the value for 'a': "))
b = float(input("Enter the value for 'b': "))
c = float(input("Enter the value for 'c': "))

# Predict outcome
predicted_outcome = predict_outcome(a, b, c)

# Display the predicted outcome
print(f"The predicted outcome is: {round(predicted_outcome)}")
