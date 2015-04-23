from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


engine = create_engine('sqlite:///temp.sqlite')
 
session = sessionmaker()
session.configure(bind=engine)
session = session()

def drop_all():
	Base.metadata.drop_all(engine)

def create_all():
	Base.metadata.create_all(engine)