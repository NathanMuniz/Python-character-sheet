from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


class FactoryConnection():
    
    def connect(self):
        BASE_DIR = os.path.dirname(os.path.realpath(__file__))
        connection_string="sqlite:///"+os.path.join(BASE_DIR, 'site.db')
        engine = create_engine(connection_string, echo=True)
        return engine
    
    def create_session(self):
        connection = self.connect()
        session = sessionmaker()
        session.configure(bind=connection)
        session_make = session()

        return session_make

