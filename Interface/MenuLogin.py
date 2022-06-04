class MenuLogin():

    def __init__(self):
        self.user_list = []



    def login(self, index):
        ## Consulta no banco de dado, e retornará o usuário 
        ## Esse usuário será passado para o MeuCharacter e retonará
        pass

    def get_users(self):
        self.user_list = ["User 1", "User 2", "User 3"]
        return self.user_list

    def show_user(self):
        ## Consulta no db, mostra nome de todos usuários 
        for user in self.user_list:
            print(user)

        

    def menu(self):
        print('-=' * 50)
        print('LOGIN PAGE')
        print('-=' * 50)
        self.show_user()
        print('-=' * 50)
       

        

        