from os import environ

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

if 'SQLALCHEMY_DATABASE_URI' not in environ:
    load_dotenv()

engine = create_engine(environ['SQLALCHEMY_DATABASE_URI'])
session_factory = sessionmaker(bind=engine)


def get_session():
    return session_factory()
