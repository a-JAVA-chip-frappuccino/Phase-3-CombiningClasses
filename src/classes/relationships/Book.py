class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

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
        if type(author) == str and len(author) > 4:
            self._author = author
        else:
            raise Exception("The author must be a string of greater than 4 characters!")
        
    author = property(get_author, set_author)