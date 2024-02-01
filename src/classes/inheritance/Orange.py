from Cat import Cat

class Orange(Cat):

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
        
    def meow(self):
        print("I am an orange cat!")
        
franklin = Cat("Franklin", 13)
timmy = Orange("Timmy", 4, "orange")

franklin.meow()
timmy.meow()