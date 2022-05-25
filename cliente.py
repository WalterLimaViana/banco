
class Cliente:

    def __init__(self, nome):
        self.__nome = nome

        #Outra forma de usar o Getter:
        @property
        def nome(self):
            return self.__nome.title()
        #Outra forma de usar o Setter:
        @nome.setter
        def nome(self, nome):
            self.__nome = nome