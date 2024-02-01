from Cat import Cat

class Void(Cat):

    def __init__(self, name, age, color):
        super().__init__(name, age)
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
        
    def hide_in_shadows(self):
        print(f"{self.name} is hiding in the shadows!")
        
franklin = Cat("Franklin", 13)
roswell = Void("Roswell", 6, "black")

roswell.hide_in_shadows()
# franklin.hide_in_shadows()