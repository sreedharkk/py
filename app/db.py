import os

from sqlalchemy import (Column, DateTime, Integer, String, Table, create_engine, MetaData)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from databases import Database

# Database url if none is passed the default one is used
#DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:12345678@localhost/fastapi")
#DATABASE_URL = "postgresql://postgres:admin1234@localhost/users"
DATABASE_URL = "postgresql://pgadmin:Admin$1234@mockapipgserver.postgres.database.azure.com/postgres"
# SQLAlchemy
engine = create_engine(DATABASE_URL)
Base = declarative_base()
metadata = MetaData()
user = Table("user", metadata,
    Column("user_id", Integer, primary_key=True),
    Column("short_name", String(50)),
    Column("first_name", String(50)),
    Column("last_name", String(50)),
    Column("photo_url", String(50)),
    Column("date_created", DateTime, default=func.now(), nullable=False),
    Column("date_modified", DateTime, default=func.now(), nullable=False)
    
)

# Databases query builder
database = Database(DATABASE_URL)
print("type of user", type(user))
print("user ", user)
print("printing database object....")
print("print database", database)
