from typing import Any, List
from fastapi import APIRouter, Depends,status
from fastapi import HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from domains.auth.schemas import user_account as schemas
from domains.auth.services.user_account import users_forms_service as actions
from db.session import get_db


users_router = APIRouter(
       prefix="/users",
    tags=["Users Account"],
    responses={404: {"description": "Not found"}},
)





@users_router.get(
    "/all",
    response_model=List[schemas.UserSchema]
)
def list_users(
        db: Session = Depends(get_db),

        skip: int = 0,
        limit: int = 100
) -> Any:
    users_router = actions.list_users_forms(db=db, skip=skip, limit=limit)
    return users_router


@users_router.post(
    "/",
    response_model=schemas.UserSchema,
    status_code=status.HTTP_201_CREATED
)
async def create_user(
    users_forms_in: schemas.UserCreate,
        db: Session = Depends(get_db)
) -> Any:
    # Await the async create_user function
    user = await actions.create_user(db=db, users_form=users_forms_in)
    return user


@users_router.put(
    "/{id}",
    response_model=schemas.UserSchema
)
def update_users(
        *, db: Session = Depends(get_db),

        id: UUID4,
        users_forms_in: schemas.UserUpdate,
) -> Any:
    users_router = actions.get_user_by_id(db=db, id=id)
    if not users_router:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail="users_forms_router not found"
        )
    users_router = actions.update_users_forms(db=db, id=users_router.id, users_form=users_forms_in)
    return users_router


@users_router.get(
    "/{id}",
    response_model=schemas.UserSchema
)
def get_users(
        *, db: Session = Depends(get_db),

        id: UUID4
) -> Any:
    users_router = actions.get_users_forms(db=db, id=id)
    if not users_router:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail="users_forms_router not found"
        )
    return users_router


@users_router.delete(
    "/{id}",
    response_model=schemas.UserSchema
)
def delete_users(
        *, db: Session = Depends(get_db),

        id: UUID4
) -> Any:
    users_forms_router = actions.get_users_forms(db=db, id=id)
    if not users_forms_router:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail="users_forms_router not found"
        )
    users_router = actions.delete_users_forms(db=db, id=id)
    return users_router