from datetime import datetime

from fastapi.encoders import jsonable_encoder
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get(
            self,
            obj_id: int,
            session: AsyncSession,
    ):
        db_obj = await session.execute(
            select(self.model).where(
                self.model.id == obj_id
            )
        )
        return db_obj.scalars().first()

    async def get_by_name(
            self,
            obj_name: str,
            session: AsyncSession,
    ):
        db_obj = await session.execute(
            select(self.model).where(
                self.model.name == obj_name
            )
        )
        return db_obj.scalars().first()

    async def update(
            self,
            db_obj,
            obj_in,
            session: AsyncSession,
    ):
        obj_data = jsonable_encoder(db_obj)
        update_data = obj_in.dict(exclude_unset=True)
        if 'full_amount' in update_data.keys() and db_obj.invested_amount == update_data['full_amount']:
            setattr(db_obj, 'fully_invested', True)
            setattr(db_obj, 'close_date', datetime.now())
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])

        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def remove(
            self,
            db_obj,
            session: AsyncSession,
    ):
        await session.delete(db_obj)
        await session.commit()
        return db_obj

    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession,
    ) -> list[dict[str, str]]:
        projects = await session.execute(
            select([CharityProject.name,
                    (func.julianday(CharityProject.close_date) -
                     func.julianday(CharityProject.create_date)
                     ).label('completion_rate'),
                    CharityProject.description
                    ]).where(
                CharityProject.fully_invested == True # noqa
            ).order_by('completion_rate')
        )
        return projects


charity_project_crud = CRUDCharityProject(CharityProject)