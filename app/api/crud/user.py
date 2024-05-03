from app.api.models.user import UserSchema
from app.db import user, database

async def post(payload: UserSchema):
    query = user.insert().values(user_id=payload.user_id, short_name=payload.short_name, first_name=payload.first_name, last_name=payload.last_name, photo_url=payload.photo_url, date_created=payload.date_created, date_modified=payload.date_modified )
    return await database.execute(query)

async def get(user_id: int):
    query = user.select().where(user_id == user.c.user_id)
    return await database.fetch_one(query)    

async def get_all():
    query = user.select()
    return await database.fetch_all(query)


async def put(user_id:int, payload=UserSchema):
    query = (
        user.update().where(user_id == user.c.user_id).values(user_id=payload.user_id, short_name=payload.short_name, first_name=payload.first_name, last_name=payload.last_name, photo_url=payload.photo_url, date_created=payload.date_created, date_modified=payload.date_modified )
        .returning(user.c.user_id)
    )
    return await database.execute(query)

async def delete(user_id:int):
    query = user.delete().where(user_id == user.c.user_id)
    return await database.execute(query)
    