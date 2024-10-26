from app.core.config import settings
from sqlmodel import create_engine, Session

database_url = settings.database_url

def get_engine(url: str = database_url):
    return create_engine(url, echo=True)

def get_session():
    with Session(get_engine()) as session:
        yield session
        

