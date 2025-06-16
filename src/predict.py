import joblib
import pandas as pd

model = joblib.load('models/xgb_model.pkl')

# Load training column names
with open('models/training_columns.txt', 'r') as f:
    training_columns = f.read().splitlines()

def predict_churn(data: dict):
    df = pd.DataFrame([data])

    # Separate numeric and categorical columns
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    df_encoded = pd.get_dummies(df, columns=categorical_cols)

    # Add missing columns
    for col in training_columns:
        if col not in df_encoded.columns:
            df_encoded[col] = 0

    df_encoded = df_encoded[training_columns]

    return model.predict(df_encoded)[0]
