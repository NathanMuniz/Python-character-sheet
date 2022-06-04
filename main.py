from Interface import MenuPrincipal
from Interface.SubMenus import SubMenuAtributo
from Interface.SubMenus import SubMenuPericias

## Menu Principal
menu_princiapal = MenuPrincipal.MenuPrinciapal()
menu_princiapal.top()
menu_princiapal.add_sub_menu(SubMenuAtributo.SubMenuAtributo(), SubMenuPericias.SubMenuPericias())
menu_princiapal.show_sub_menu()
menu_princiapal.open_sub_menu(0)
