class SubMenuPericias():
    def __init__(self, name="Pericias"):
        self.name = name 
    
    def top(self):
        print('PERÍCIAS')
        print(50 * "-")
        print('This is the Pericias')
        print(50 * "-")
    
    def get_name(self):
        return self.name

    def open_menu(self):
        return self.top()