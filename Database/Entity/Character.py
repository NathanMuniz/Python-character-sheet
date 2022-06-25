from datetime import date
current_date = date.today()


class Character():
        def __init__(self, name):
            self.__name = name
            self.__creation_date = current_date

        @property
        def name(self):
            return self.__name

        @property
        def creation_date(self):
            return self.__creation_date

        def show_datas(self):
            return f"name: {self.__name}, Date: {self.__creation_date}"
