from typing import List

from fastapi import APIRouter

from db.models.trade import Trade

operations_router = APIRouter(prefix="/operations")

fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12},
]


@operations_router.post()
async def add_trades(trades: List[Trade]):
