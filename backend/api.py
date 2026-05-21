from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services import calculate

router = APIRouter()

class CalculationRequest(BaseModel):
    operation: str
    num1: float
    num2: float

class CalculationResponse(BaseModel):
    result: float

@router.post("/calculate", response_model=CalculationResponse)
async def perform_calculation(request: CalculationRequest):
    try:
        result = calculate(request.operation, request.num1, request.num2)
        return CalculationResponse(result=result)
    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")