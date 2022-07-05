from Database.Factory import FactoryConnection
from Database.Factory.db import Character

factory = FactoryConnection.FactoryConnection()

class CharacterQuery():

    def new_character(self, character, session):
        session.add(character)

    def character_list(self, session):
        character = session.query(Character).all()
        return character
    
    def id_search(self, character_id, session):
        character = session.query(Character).filter(Character._id == character_id).first()
        return character