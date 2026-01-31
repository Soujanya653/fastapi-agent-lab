from fastapi import FastAPI, HTTPException
from schemas import CalculatorInput
from agent import CalculatorAgent

app = FastAPI(title="Calculator Agent")

agent = CalculatorAgent()

@app.post("/calculate")
def calculate(data: CalculatorInput):
    try:
        result = agent.process(data.operation, data.a, data.b)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
