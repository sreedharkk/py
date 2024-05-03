from typing import Any, List
from fastapi import APIRouter, HTTPException, Path, FastAPI

from app.api.crud import user
from app.api.models.user import UserSchema,UserDB

router = APIRouter()


@router.post("/", response_model=UserDB, status_code=201)
async def create_user(payload: UserSchema):
    user_id = await user.post(payload)

    response_object = {
        "usr_id": user_id,
        "short_name": payload.short_name,
        "first_name": payload.first_name,
        "last_name": payload.last_name,
        "photo_url": payload.photo_url,
        "date_created": payload.date_created,
        "date_modified": payload.date_modified,
    }
    return response_object
    
@router.get("/{user_id}/", response_model=UserDB)
async def read_user(user_id: int = Path(..., gt=0),):
    user = await user.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user

@router.get("/", response_model=List[UserDB])
async def read_all_users():
    return await user.get_all()

@router.put("/{user_id}/", response_model=UserDB)
async def update_user(payload:UserSchema,id:int=Path(...,gt=0)): #Ensures the input is greater than 0
    user = await user.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user_id = await user.put(user_id, payload)
    response_object = {
        "id": user_id,
        "title": payload.title,
        "description": payload.description
    }
    return response_object

#DELETE user
@router.delete("/{user_id}/", response_model=UserDB)
async def delete_user(user_id:int = Path(...,gt=0)):
    user = await user.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    await user.delete(user_id)

    return user
