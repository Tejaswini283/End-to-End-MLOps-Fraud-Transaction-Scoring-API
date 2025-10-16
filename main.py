from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Initialize the FastAPI app
app = FastAPI()

# Load the trained model
model = joblib.load('fraud_model.joblib')

# Define the input data structure using Pydantic
class Transaction(BaseModel):
    # The model expects 30 features (V1-V28, Time, Amount)
    # We'll represent them as a list of floats for simplicity
    features: list[float]

@app.get("/")
def read_root():
    return {"message": "Credit Card Fraud Detection API"}

@app.post("/predict")
def predict_fraud(transaction: Transaction):
    # Convert input data to a DataFrame
    input_df = pd.DataFrame([transaction.features])
    # The model was trained on features without names, so we can pass it directly

    # Make a prediction
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1] # Prob of being fraud

    # Determine the result
    is_fraud = "Fraud" if prediction == 1 else "Not Fraud"

    return {
        "prediction": is_fraud,
        "probability": float(probability)
    }