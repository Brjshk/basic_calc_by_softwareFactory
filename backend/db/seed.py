from sqlalchemy.orm import Session
from models import Calculation

def seed_calculations(db: Session):
    calculations = [
        Calculation(operation='add', num1=1, num2=2, result=3),
        Calculation(operation='subtract', num1=5, num2=3, result=2),
        Calculation(operation='multiply', num1=4, num2=2, result=8),
        Calculation(operation='divide', num1=10, num2=2, result=5)
    ]
    db.add_all(calculations)
    db.commit()
