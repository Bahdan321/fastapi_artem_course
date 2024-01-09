from pydantic import BaseModel

class Trade(BaseModel);
    id: int
    user_id: int
    currency: str
    price: float
    amount: float