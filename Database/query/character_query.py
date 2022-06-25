from factory import factoryconnection 
from factory.db import Character

factory = factoryconnection.FactoryConnection()

class CharacterQuery():

    def new_character(self, character, session):
        session.add(character)
    
    def character_list()

