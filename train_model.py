import pandas as pd
from sklearn.model_selection import train_test_split
from lightgbm import LGBMClassifier
import joblib

# Load the dataset from Kaggle
data = pd.read_csv('creditcard.csv')

# Prepare the data
X = data.drop('Class', axis=1)
y = data['Class']

# We'll use the full dataset for a "production" model for simplicity
# In a real project, you'd use a proper train/test split for evaluation
print("Training LightGBM model...")
model = LGBMClassifier(objective='binary', random_state=42)
model.fit(X, y)

# Save the trained model to a file
joblib.dump(model, 'fraud_model.joblib')

print("Model trained and saved as fraud_model.joblib")