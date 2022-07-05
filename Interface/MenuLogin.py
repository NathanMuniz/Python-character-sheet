from Database.Repository import CharacterRepository
from Database.Factory.FactoryConnection import FactoryConnection
from time import sleep


factory = FactoryConnection()
characterRepo = CharacterRepository.CharacterRepository()
sn = factory.create_session()

class MenuLogin():

    def __init__(self):
        self.characters = self.get_characters()
        self.name = "Login"

    def login(self, index):
        ## Consulta no banco de dado, e retornará o usuário 
        ## Esse usuário será passado para o MenuCharacter e retonará
        pass

    def get_name(self):
        return self.name

    def get_characters(self):
        characters = characterRepo.characters(sn)
        return characters


    def show_characters(self):
        ## Consulta no db, mostra nome de todos usuários 
        for character in self.characters:
            print(character)

    def get_character(self, id):
        character = characterRepo.search_id(id, sn)
        sn.close()
        return character.name

    def open_menu(self):
        print('-=' * 50)
        print('LOGIN PAGE')
        print('-=' * 50)
        sleep(1)
        self.show_characters()
        sleep(1)
        choice = -1
        while True:
            if(choice < 0 or choice > len(self.characters)):
                choice = int(input('What user do u want'))
            else:
                print(self.get_character(choice))
                break

        print('-=' * 50)
       

        

        