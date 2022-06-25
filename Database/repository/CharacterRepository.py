from Database.Query import CharacterQuery
from Database.Factory.db import Character

class CharacterRepository():
    def __init__(self,):
        self.characters = self.characters

    def new_character(self, character, session):
        query_character = CharacterQuery.CharacterQuery()
        new_character = Character(name=character.name, creation_date=character.creation_date)
        query_character.new_character(new_character, session)

    def characters(self):
        pass