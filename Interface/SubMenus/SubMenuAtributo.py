class SubMenuAtributo():
    def __init__(self, name="Atributos"):
        self.name = name 
    
    def top(self):
        print(50 * "-")
        print('This is the SubMenuTeste')
        print(50 * "-")

    def show_pericias(self):
        print("Velocidade - 23")
    
    def get_name(self):
        return self.name
    
    def open_menu(self):
        return self.top(), self.show_pericias()

