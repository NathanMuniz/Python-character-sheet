from Database.Factory import FactoryConnection
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Text


factory = FactoryConnection.FactoryConnection()
engine = factory.connect()

Base = declarative_base()

class Character(Base):
    __tablename__ = "character"

    _id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    creation_date = Column(Date, nullable=False)
    
    def __repr__(self):
        return f"Id: {self._id} Name: {self.name}"


#Base.metadata.create_all(engine)