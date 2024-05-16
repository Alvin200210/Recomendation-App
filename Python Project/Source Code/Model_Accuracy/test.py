import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

# Load the dataset
df = pd.read_csv("dataset.csv")

# Separate features (X) and target variable (y)
X = df.drop(columns=[
    "Do you prefer a structured or flexible work environment?",
    "Are you more comfortable with a formal or casual work atmosphere?",
    "How do you prefer to collaborate with colleagues?",
    "Are you more productive when working independently or as part of a team?",
    "Do you prefer a hands-on, directive management style, or do you prefer more autonomy and freedom?",
    "How do you respond to feedback and guidance from supervisors?",
    "How important is work-life balance to you, and what initiatives or policies do you appreciate in this regard?",
    "What values do you prioritize in a workplace?",
    "How important is it for you to work for a company that aligns with your personal values and beliefs?",
    "What are your expectations regarding career development opportunities within a company?",
    "How do you respond to constructive feedback, and what type of feedback culture do you thrive in?",
    "How do you prefer to celebrate successes and achievements in the workplace?"
])
y = df["Company"]

# Define categorical features
categorical_features = X.columns

# Define preprocessing pipeline for categorical features
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), categorical_features)
    ])

# Define the model pipeline
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model_pipeline.fit(X_train, y_train)

# Evaluate the model
accuracy = model_pipeline.score(X_test, y_test)
print(f"Model accuracy: {accuracy}")

# Save the trained model to a file
joblib.dump(model_pipeline, "random_forest_model.pkl")
