from domains.auth.models.users import APIBase
from domains.auth.models.refresh_token import APIBase
from db.session import engine
from sqlalchemy import MetaData


def create_tables():
    APIBase.metadata.create_all(bind=engine)

    #APIBase.metadata.drop_all(bind=engine)

   

