from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, PositiveInt


class DonationBase(BaseModel):
    full_amount: Optional[PositiveInt]
    comment: Optional[str]


class DonationCreate(DonationBase):
    full_amount: PositiveInt


class DonationDB(DonationBase):
    id: int
    invested_amount: Optional[int] = Field(0)
    fully_invested: Optional[bool] = Field(False)
    create_date: Optional[datetime]
    close_date: Optional[datetime]
    user_id: Optional[int]

    class Config:
        orm_mode = True