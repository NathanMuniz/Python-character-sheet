from Interface import MenuCharacter
from Interface.SubMenus import SubMenuAtributo
from Interface.SubMenus import SubMenuPericias
from Interface import  MenuLogin 
from time import sleep


##LOGIN
menu_login = MenuLogin.MenuLogin()
menu_login.menu()
choice = -1
while True:
    if choice > len(menu_login.get_users()) or choice < 0:
        choice = int(input('What Character do you want: '))
    else:
        print(len(menu_login.get_users()))
        print("LOADING...")
        sleep(4)
        break
user = menu_login.Login(choice)





## Menu Principal
menu_character = MenuCharacter.MenuCharacter(user)
menu_character.top()
menu_character.add_sub_menu(SubMenuAtributo.SubMenuAtributo(), SubMenuPericias.SubMenuPericias())
menu_character.show_sub_menu()
enter = -1

while True: 
    if(enter < 0 or enter > len(menu_character.sub_menus) - 1):
        enter = int(input('What menu do you wanna in: '))
    else: 
        break

menu_character.open_sub_menu(enter)

