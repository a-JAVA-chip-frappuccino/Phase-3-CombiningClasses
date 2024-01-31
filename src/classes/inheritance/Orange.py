class Orange():

    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        if type(color) == str:
            self._color = color
        else:
            raise Exception