from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud import donation_crud
from app.models import CharityProject, User
from app.schemas.donation import DonationCreate, DonationDB
from app.services.investment import investment

router = APIRouter()


@router.get(
    '/',
    response_model_exclude_none=True,
    response_model=list[DonationDB],
    dependencies=[Depends(current_superuser)],
)
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session),
):
    """Superuser only."""
    return await donation_crud.get_multi(session)


@router.get(
    '/my',
    response_model_exclude_none=True,
    response_model=list[DonationDB],
    response_model_exclude={
        'close_date',
        'user_id',
        'fully_invested',
        'invested_amount'
    }
)
async def get_user_donations(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    return await donation_crud.get_by_user(user, session)


@router.post(
    '/',
    response_model_exclude_none=True,
    response_model=DonationDB,
    response_model_exclude={
        'close_date',
        'user_id',
        'fully_invested',
        'invested_amount'
    }
)
async def create_donation(
    donation: DonationCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    new_donation = await donation_crud.create(
        donation, session, user
    )
    return await investment(new_donation, CharityProject, session)
