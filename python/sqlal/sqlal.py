from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import db
from db import Base

class Parent(Base):
	__tablename__ = 'parent'
	id = Column(Integer, primary_key=True)
	#children = relationship('Child')

class Child(Base):
	__tablename__ = 'child'
	id = Column(Integer, primary_key=True)
	parent_id = Column(Integer, ForeignKey('parent.id'))
	parent = relationship('Parent', backref=backref('children'))

db.drop_all()
db.create_all()

parent = Parent()
child_1 = Child()
child_2 = Child()

db.session.add(parent)
db.session.add(child_1)
db.session.add(child_2)
db.session.commit()

print(parent.children)