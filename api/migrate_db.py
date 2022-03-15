from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
load_dotenv()

from api.db import Base
from api.models.task import Task, Done

# DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8"
DB_URL = os.environ['DATABASE_URL']

engine = create_engine(DB_URL, echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()
