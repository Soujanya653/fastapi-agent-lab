from pydantic import BaseModel

class CalculatorInput(BaseModel):
    operation: str
    a: float
    b: float
