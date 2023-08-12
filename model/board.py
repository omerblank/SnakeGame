class Board:
    def __init__(self, size, color):
        self._size = size
        self._color = color

    def get_size(self):
        return self._size

    def get_color(self):
        return self._color

    def set_type(self, new_size):
        self._size = new_size

    def set_effectiveness(self, new_color):
        self._color = new_color
