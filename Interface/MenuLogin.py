class MenuLogin():

    def __init__(self):
        self.character_list = []



    def login(self, index):
        ## Consulta no banco de dado, e retornará o usuário 
        ## Esse usuário será passado para o MenuCharacter e retonará
        pass

    def get_characters(self):
        self.character_list = ["Character 1", "Character 2", "Character 3"]
        return self.character_list

    def show_character(self):
        ## Consulta no db, mostra nome de todos usuários 
        for character in self.character_list:
            print(character)

        

    def menu(self):
        print('-=' * 50)
        print('LOGIN PAGE')
        print('-=' * 50)
        self.show_character()
        print('-=' * 50)
       

        

        