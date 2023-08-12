class Food:
    def __init__(self, type, effectiveness):
        self.__type = type
        self.__effectiveness = effectiveness

    def get_type(self):
        return self.__type

    def get_effectiveness(self):
        return self.__effectiveness

    def set_type(self, new_type):
        self.__type = new_type

    def set_effectiveness(self, new_effectiveness):
        self.__effectiveness = new_effectiveness
