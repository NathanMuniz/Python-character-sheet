class SubMenuAtributo():
    def __init__(self, name="Atributos"):
        self.name = name 
    
    def top(self):
        print(50 * "-")
        print('This is the SubMenuTeste')
        print(50 * "-")
    
    def get_name(self):
        return self.name
    
    def open_menu(self):
        self.top()

