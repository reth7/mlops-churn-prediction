import pandas as pd
import xgboost as xgb
import joblib
import mlflow
import mlflow.xgboost
from mlflow.models.signature import infer_signature

# Load dataset
df = pd.read_csv('data/telco_churn.csv')

# Basic preprocessing
df = df.dropna()
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

X = df.drop(['customerID', 'Churn'], axis=1)
# Identify categorical and numeric columns
categorical_cols = X.select_dtypes(include=['object']).columns.tolist()
numeric_cols = X.select_dtypes(exclude=['object']).columns.tolist()

# Encode only categoricals
X_encoded = pd.get_dummies(X, columns=categorical_cols)
input_example = X_encoded.iloc[:5]
# Save the training columns
with open('models/training_columns.txt', 'w') as f:
    for col in X_encoded.columns:
        f.write(col + '\n')

y = df['Churn']

# Train model
model = xgb.XGBClassifier(eval_metric='logloss')
model.fit(X_encoded, y)

# Save locally
joblib.dump(model, 'models/xgb_model.pkl')

signature = infer_signature(X_encoded, model.predict(X_encoded))
# MLflow logging
mlflow.set_experiment("ChurnPrediction")
with mlflow.start_run():
    mlflow.xgboost.log_model(model, "model", signature=signature, input_example=input_example)
    mlflow.log_params(model.get_params())
    mlflow.log_metric("accuracy", model.score(X_encoded, y))
