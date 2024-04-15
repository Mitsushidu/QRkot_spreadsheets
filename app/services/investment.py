from datetime import datetime
from typing import Union

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import CharityProject, Donation


async def investment_cycle(
    new_object: Union[CharityProject, Donation],
    db_objects: Union[CharityProject, Donation],
) -> None:
    """Функция распределения пожертвований."""
    new_object_full = new_object.full_amount
    new_object_invested = 0

    for object in db_objects:

        object_full = object.full_amount
        object_invested = object.invested_amount
        object_left = object_full - object_invested

        if new_object_invested + object_left >= new_object_full:
            object_invested_new = object_full - (new_object_invested + object_left - new_object_full)
            new_object_invested += object_invested_new - object_invested
            setattr(object, 'invested_amount', object_invested_new)
            if object_full == object_invested_new:
                setattr(object, 'fully_invested', True)
                setattr(object, 'close_date', datetime.now())
            setattr(new_object, 'invested_amount', new_object_invested)
            setattr(new_object, 'fully_invested', True)
            setattr(new_object, 'close_date', datetime.now())
            break

        else:
            new_object_invested += object_left
            setattr(new_object, 'invested_amount', new_object_invested)
            setattr(object, 'invested_amount', object_full)
            setattr(object, 'fully_invested', True)
            setattr(object, 'close_date', datetime.now())


async def investment(
    new_object: Union[CharityProject, Donation],
    db_model: Union[CharityProject, Donation],
    session: AsyncSession,
) -> CharityProject:
    """Функция для инвестирования проектов и донатов."""
    db_objects = await session.execute(
        select(db_model).where(
            db_model.fully_invested == False # noqa
        )
    )
    db_objects: list[db_model] = db_objects.scalars().all()

    if db_objects is None:
        return new_object

    await investment_cycle(
        new_object,
        db_objects
    )

    await session.commit()
    await session.refresh(new_object)
    return new_object