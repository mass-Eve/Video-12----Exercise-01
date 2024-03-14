from book_class import Book

class Library:
    def __init__(self):
        self.books_catalogue = list()

    def updateCatalogue(self, *books : tuple):
        for book in books:
            self.books_catalogue.append(book)

    def showCatalogue(self):
        print(self.books_catalogue)

# lib = Library()
# lib.updateCatalogue('Harry Potter', 'Ronald Wesely', 'Hermoine Granger', "Hegret")
# lib.showCatalogue()