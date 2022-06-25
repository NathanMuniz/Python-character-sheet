class MenuCharacter():

    def __init__(self, character):
        self.sub_menus = []
        self.character = character
        
    
    def top(self):
        print('RPG')
        print('-' * 50)
        print(f'Pefil do Investigado {self.character.name}')
        print('-' * 50)
    
    def add_sub_menu(self, *sub_list):
        for menu in sub_list:
            self.sub_menus.append(menu)
    
    def show_sub_menu(self, pos=-1):
        if pos==-1:
            for pos, menu in enumerate(self.sub_menus):
                print(f"{menu.get_name()}[{pos}]")
        else: 
            print(self.sub_menus[pos])
    
    def open_sub_menu(self, pos=-1):
        if pos==-1:
            for menu in self.sub_menus():
                menu.open_sub_menu()
        else: 
            return self.sub_menus[pos].open_menu()
        




    


