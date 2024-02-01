class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

        self._owner = None

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if type(title) == str:
            self._title = title
        else:
            raise Exception("The title must be a string!")
        
    def get_author(self):
        return self._author
    
    def set_author(self, author):
        if type(author) == str and len(author) > 4 and not hasattr(self, 'author'):
            self._author = author
        else:
            raise Exception("The author must be a string of greater than 4 characters and cannot be reset!")
        
    author = property(get_author, set_author)

    def get_owner(self):
        return self._owner
    
    def set_owner(self, new_owner):
        from Owner import Owner
        if isinstance(new_owner, Owner):
            self._owner = new_owner
        else:
            raise Exception("The owner must be an instance of the Owner class!")
        
    owner = property(get_owner, set_owner)

    def turn_the_page(self):
        print("Flipping to the next page of " + self.title + ".")

    def __str__(self):
        return f"Title: {self.title} Author: {self.author}"