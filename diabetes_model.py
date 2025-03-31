import pandas as pd
import numpy as np
from scipy.stats import skew
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load and preprocess the data
def preprocess_data():
    df = pd.read_csv('diabetes_prediction_dataset.csv')

    df.drop_duplicates(inplace=True)
    df = df[df["gender"] != "Other"]

    # Stratified random sampling to ensure equal distribution of labels
    num_classes = df['diabetes'].nunique()
    samples_per_class = 1000 // num_classes
    selected_data = df.groupby('diabetes', group_keys=False).apply(lambda x: x.sample(n=samples_per_class, random_state=100))

    if len(selected_data) < 1000:
        additional_samples = df.drop(selected_data.index).sample(n=1000 - len(selected_data), random_state=42)
        selected_data = pd.concat([selected_data, additional_samples])

    df = selected_data.sample(frac=1, random_state=42).reset_index(drop=True)

    df.drop(columns=['smoking_history'], inplace=True)

    le = LabelEncoder()
    df['gender'] = le.fit_transform(df['gender'])

    columns_to_check = ['age', 'bmi', 'HbA1c_level', 'blood_glucose_level']
    skew_values = df[columns_to_check].apply(lambda x: skew(x))

    columns_to_transform = skew_values[abs(skew_values) > 0.5].index
    df[columns_to_transform] = df[columns_to_transform].apply(lambda x: np.log1p(x))

    return df

# Train the model
def train_model():
    df = preprocess_data()

    x = df[['gender', 'age', 'hypertension', 'heart_disease', 'bmi', 'HbA1c_level', 'blood_glucose_level']]
    y = df['diabetes']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    rf = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        min_samples_split=5,
        min_samples_leaf=3,
        max_features="sqrt",
        random_state=42
    )

    rf.fit(x_train, y_train)

    train_accuracy = rf.score(x_train, y_train)
    test_accuracy = rf.score(x_test, y_test)

    print(f"Train Accuracy: {train_accuracy:.4f}")
    print(f"Test Accuracy: {test_accuracy:.4f}")

    # Save the trained model to a file
    pickle.dump(rf, open('diabetes_model.pkl', 'wb'))

# Call the function to train and save the model
if __name__ == "__main__":
    train_model()
