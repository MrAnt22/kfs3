from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class WeatherData(Base):
    __tablename__ = 'weather_data'

    id = Column(Integer, primary_key=True, index=True)
    datetime = Column(DateTime, nullable=False)       
    temperature = Column(Float, nullable=True)         
    humidity = Column(Float, nullable=True)            
    wind_speed = Column(Float, nullable=True)          
    air_quality_index = Column(Float, nullable=True)   
    location = Column(String(255), nullable=True) 

    def __repr__(self):
        return f"<WeatherData(id={self.id}, datetime={self.datetime}, AQI={self.air_quality_index})>"
