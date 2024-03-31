from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CountriesToContinent(Base):
    __tablename__ = 'countries_to_continent'
    id = Column(Integer, primary_key=True)
    continent = Column(String)
    country = Column(String)

class ConfirmedCases(Base):
    __tablename__ = 'covid_confirmed'
    id = Column(Integer, primary_key=True)
    province_state = Column(String)
    country_region = Column(String, ForeignKey('countries_to_continent.country'))
    lat = Column(Float)
    long = Column(Float)
    date = Column(Date)
    confirmed = Column(Integer)
 
    # Define relationship to CountriesToContinent
    country_continent = relationship('CountriesToContinent', backref='confirmed_cases')

class RecoveredCases(Base):
    __tablename__ = 'covid_recovered'
    id = Column(Integer, primary_key=True)
    province_state = Column(String)
    country_region = Column(String, ForeignKey('countries_to_continent.country'))
    lat = Column(Float)
    long = Column(Float)
    date = Column(Date)
    recovered = Column(Integer)
    
    # Define relationship to CountriesToContinent
    country_continent = relationship('CountriesToContinent', backref='recovered_cases')
