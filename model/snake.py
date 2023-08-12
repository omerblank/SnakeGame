class Snake:
    def __init__(self, color, length):
        self._color = color
        self._length = length

    def get_color(self):
        return self._color

    def get_length(self):
        return self._length

    def set_color(self, new_color):
        self._color = new_color

    def set_length(self, new_length):
        self._length = new_length
