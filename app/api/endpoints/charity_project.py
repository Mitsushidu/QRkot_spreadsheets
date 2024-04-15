from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud import charity_project_crud
from app.models import Donation
from app.schemas.charity_project import (CharityProjectCreate,
                                         CharityProjectDB,
                                         CharityProjectUpdate)
from app.services.investment import investment

from .validators import (check_amount, check_charity_project_before_delete,
                         check_charity_project_before_update,
                         check_charity_project_exists,
                         check_charity_project_name_duplicate)

router = APIRouter()


@router.get(
    '/',
    response_model_exclude_none=True,
    response_model=list[CharityProjectDB],
)
async def get_all_charity_projects(
    session: AsyncSession = Depends(get_async_session)
):
    return await charity_project_crud.get_multi(session)


@router.post(
    '/',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser), ],
)
async def create_charity_project(
    charity_project: CharityProjectCreate,
    session: AsyncSession = Depends(get_async_session)
):
    """Superuser only."""
    await check_charity_project_name_duplicate(charity_project.name, session)
    new_charity_project = await charity_project_crud.create(charity_project, session, None)
    return await investment(new_charity_project, Donation, session)


@router.delete(
    '/{project_id}',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser), ],
)
async def delete_charity_project(
    project_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    """Superuser only."""
    charity_project = await check_charity_project_exists(project_id, session)
    await check_charity_project_before_delete(charity_project)
    return await charity_project_crud.remove(charity_project, session)


@router.patch(
    '/{project_id}',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser), ],
)
async def partially_update_charity_project(
    project_id: int,
    obj_in: CharityProjectUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    """Superuser only."""
    charity_project = await check_charity_project_exists(project_id, session)
    await check_charity_project_before_update(charity_project)
    if obj_in.name is not None:
        await check_charity_project_name_duplicate(obj_in.name, session)
    if obj_in.full_amount is not None:
        await check_amount(charity_project, obj_in.full_amount)
    return await charity_project_crud.update(
        charity_project,
        obj_in,
        session
    )
