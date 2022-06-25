from Database.Factory import FactoryConnection
from Database.Factory.db import Character

factory = FactoryConnection.FactoryConnection()

class CharacterQuery():

    def new_character(self, character, session):
        session.add(character)

    def character_list(self, session):
        character = session.query(Character).all()
        return character
    
