# sandbox environment for testing purposes

from Book import Book
from Owner import Owner

jungle = Book("The Jungle", "Upton Sinclair")
gatsby = Book("The Great Gatsby", "F. Scott Fitzgerald")
quixote = Book("Don Quixote", "Miguel de Cevantes Saavedra")

clarice = Owner("Clarice")
mustard = Owner ("Coronel Mustard")

jungle.owner = clarice
clarice.books = jungle

gatsby.owner = clarice
clarice.books = gatsby

quixote.owner = mustard
mustard.books = quixote

print(mustard.books[0].turn_the_page())