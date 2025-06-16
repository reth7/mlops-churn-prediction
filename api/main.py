from fastapi import FastAPI
from src.schema import Customer
from src.predict import predict_churn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Churn Predictor API"}

@app.post("/predict")
def predict(customer: Customer):
    result = predict_churn(customer.dict())
    return {"churn": bool(result)}
