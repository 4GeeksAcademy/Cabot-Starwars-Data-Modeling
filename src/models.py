import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250))

class Planets(Base):
    __tablename__ = 'Planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    diameter = Column(String(250), nullable=False)
    rotational_period = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    
    def to_dict(self):
        return {}
    

class Characters(Base):
    __tablename__ = 'Characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    hair_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)

    def to_dict(self):
        return {}
    

class Favorites(Base):
    __tablename__ = 'Favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'),nullable=False)
    character_id = Column(Integer,ForeignKey('Characters.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('Planets.id'), nullable=False)
    planets = relationship(Planets)
    characters = relationship(Characters)
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
