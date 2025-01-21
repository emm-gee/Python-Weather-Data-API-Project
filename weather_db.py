from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Creates a SQLite database named weather.db
engine = create_engine("sqlite:///weather.db")
# Provides a base class for defining ORM models
Base = declarative_base()
# Creates a factory for creating sessions to interact with the database
Session = sessionmaker(bind=engine)

# Creates a table called weather_data with fields that correspond to calculated weather stats
class WeatherDataDB(Base):
    __tablename__ = "weather_data"
    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    month = Column(Integer)
    day = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)
    mean_temp = Column(Float)
    min_temp = Column(Float)
    max_temp = Column(Float)
    avg_wind_speed = Column(Float)
    min_wind_speed = Column(Float)
    max_wind_speed = Column(Float)
    sum_precip = Column(Float)
    min_precip = Column(Float)
    max_precip = Column(Float)



# Creates the table if it does not already exist
Base.metadata.create_all(engine)

