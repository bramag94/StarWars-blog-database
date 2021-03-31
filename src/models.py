import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

    def to_dict(self):
        return {}


class Characters(Base):
    __tablename__ = 'Characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))
   
    def to_dict(self):
        return {}

    

class Planets(Base):
    __tablename__ = 'Planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)
    climate = Column(String(250))
    gravity = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(Integer)
    population = Column(Integer)

    def to_dict(self):
        return {}


class Favs(Base):
    __tablename__ = 'Favoritos'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey (User.id))
    user_name = Column(String(250), ForeignKey (User.name))
    characters_id = Column(String(250), ForeignKey (Characters.id))
    planetas_id = Column(String(250), ForeignKey (Planets.id))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')