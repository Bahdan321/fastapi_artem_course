from typing import Annotated
from annotated_types import MinLen, MaxLen, Ge

from pydantic import BaseModel

class Trade(BaseModel):
    id: int
    user_id: int
    currency: Annotated[str, MinLen(3), MaxLen(25)]
    side: str
    price: Annotated[float, Ge(0)]
    amount: float