from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class FactoryConnection():
    
    def connect(self):
        engine = create_engine("sqlite+pysqlite:///:memory:")
        return engine
    
    def create_session(self):
        connection = self.connect()
        session = sessionmaker()
        session.configure(bind=connection)
        session_make = session()

        return session_make

