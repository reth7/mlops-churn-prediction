from pydantic import BaseModel

class Customer(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    InternetService: str
    MonthlyCharges: float
    TotalCharges: float
