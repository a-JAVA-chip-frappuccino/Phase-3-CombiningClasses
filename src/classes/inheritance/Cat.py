class Cat():

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    name = property(get_name, set_name)

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age

    def meow(self):
        print("I am a plain cat!")

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}"
    
nudie = Cat("Marshall", 1)

# nudie.meow()