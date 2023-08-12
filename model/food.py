class Food:
    def __init__(self, type, effectiveness):
        self._type = type
        self._effectiveness = effectiveness

    def get_type(self):
        return self._type

    def get_effectiveness(self):
        return self._effectiveness

    def set_type(self, new_type):
        self._type = new_type

    def set_effectiveness(self, new_effectiveness):
        self._effectiveness = new_effectiveness
