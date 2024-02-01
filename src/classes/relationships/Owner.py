class Owner():

    def __init__(self, name):
        self.name = name

        self._books = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, "name"):
            self._name = name
        else:
            raise Exception("Owner cannot be given a new name!")
        
    @property
    def books(self):
        return self._books
    
    @books.setter
    def books(self, new_book):
        from Book import Book
        if isinstance(new_book, Book) and new_book not in self._books:
            self._books.append(new_book)
        else:
            raise Exception("New book must be an instance of Book class and must be new to me!")
        
    def __str__(self):
        return f"Name: {self.name}"