from Interface import MenuCharacter
from Interface.SubMenus import SubMenuAtributo
from Interface.SubMenus import SubMenuPericias
from Interface import MenuLogin
from time import sleep

from Database.Repository import CharacterRepository
from Database.Factory.FactoryConnection import FactoryConnection
from Database.Entity.Character import Character

"""
factory = FactoryConnection()
sn = factory.create_session()
characterRepo = CharacterRepository.CharacterRepository()

character = characterRepo.search_id(1, sn)
print(character.name)
"""




##LOGIN
menu_login = MenuLogin.MenuLogin()

## Menu Principal
menu_character = MenuCharacter.MenuCharacter()
menu_character.top()
menu_character.add_sub_menu(menu_login)
menu_character.show_sub_menu()
enter = -1

while True: 
    if(enter < 0 or enter > len(menu_character.sub_menus) - 1):
        enter = int(input('What menu do you wanna in: '))
    else: 
        menu_character.open_sub_menu(enter)
        break





