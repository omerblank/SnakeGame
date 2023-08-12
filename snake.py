class Snake:
    def __init__(self, color, length):
        self.__color = color
        self.__length = length

    def get_color(self):
        return self.__color

    def get_length(self):
        return self.__length

    def set_color(self, new_color):
        self.__color = new_color

    def set_length(self, new_length):
        self.__length = new_length
