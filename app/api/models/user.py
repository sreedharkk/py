import datetime
from datetime import datetime
from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    user_id: int = Field(..., gt=0, lt=5000)
    short_name: str = Field(..., min_length=3, max_length=50) #additional validation for the inputs 
    first_name: str = Field(...,min_length=3, max_length=50)
    last_name: str = Field(..., min_length=3, max_length=50)
    photo_url: str = Field(..., min_length=3, max_length=50)
    date_created: datetime = datetime(2023, 3, 24).strftime("%Y-%m-%d")
    date_modified: datetime = datetime(2024, 3, 24).strftime("%Y-%m-%d")


class UserDB(UserSchema):
    user_id: int 
    short_name: str
    first_name: str
    last_name: str
    photo_url: str
    date_created: datetime
    date_modified: datetime

