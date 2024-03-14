class Library:
    def __init__(self):
        self.books_catalogue = list()

    def updateCatalogue(self, *books : list):
        for book in books:
            self.books_catalogue.append(book)

    def showCatalogue(self):
        print('Sr.    Book')
        for book in enumerate(self.books_catalogue):
            print(f"{book[0] + 1}     '{book[1]}'")

lib = Library()
lib.updateCatalogue()
lib.showCatalogue()