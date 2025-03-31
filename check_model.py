import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('diabetes_model.pkl', 'rb'))

# Define sample input (make sure it's in the correct format)
sample_input = np.array([[0, 54, 0, 0, 27.32, 6.6, 80]])  # Example of a non-diabetic person

# Make prediction
pred = model.predict(sample_input)

print("Prediction:", pred)
