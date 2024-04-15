from datetime import datetime
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import Base  # noqa
from app.models import CharityProject, Donation, User  # noqa


class CRUDBase:

    def __init__(self, model):
        self.model = model

    async def get_not_invested(
        self,
        session: AsyncSession,
    ):
        db_objs = await session.execute(
            select(
                self.model
            ).where(
                self.model.fully_invested is False
            )
        )
        return db_objs.scalars().all()

    async def get_multi(
        self,
        session: AsyncSession
    ):
        db_objs = await session.execute(select(self.model))
        return db_objs.scalars().all()

    async def create(
        self,
        obj_in,
        session: AsyncSession,
        user: Optional[User],
    ):
        obj_in_data = obj_in.dict()
        obj_in_data['create_date'] = datetime.now()
        if user is not None:
            obj_in_data['user_id'] = user.id
        db_obj = self.model(**obj_in_data)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj
