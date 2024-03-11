class Book:
    def __init__(self):
        self.book_name = str()
        self.author = str()
        self.publication_name = str()
        self.genre = str()
        self.pub_year = int()
        self.isbn_number = int()
        self.selling_price = int()
        self.total_copies = int()
        self.quantities_available = int()

    def createBook(self):
        self.book_name = bname
        self.isbn_number = ISBN
        self.selling_price = price
        self.author = writer
        self.genre = book_genre
        self.pub_year = publish_year
        self.publication_name = publication
        self.total_copies = total_number_of_copies
        self.quantities_available = available_copies_amount

    def updateBookDetails(self):
        pass

    def displayBookDetails(self):
        print(f"BOOK NAME : {self.book_name}")
        print(f"AUTHOR NAME : {self.author}")
        print(f"PUBLICATION : {self.publication_name}")
        print(f"GENRE : {self.genre}")
        print(f"PUBLICATION YEAR : {self.pub_year}")
        print(f"ISBN : {self.isbn_number}")
        print(f"PRICE : {self.selling_price}")
        print(f"TOTAL COPIES AVAILABLE IN LIBRARY : {self.total_copies}")
        print(f"TOTAL COPIES AVAIABLE TO BORROW : {self.quantities_available}")

    def checkAvaiablility(self):
        if (quantities_available > total_copies):
            print(f'Total copies available to borrow are : {self.quantities_available}')
            print("YES YOU CAN BORROW THIS BOOK !")
        else:
            print(f'Total copies available to borrow are : {self.quantities_available}')
            print("NO YOU CAN NOT BORROW THIS BOOK, ALL THE COPIES ARE IN DISTRIBUTION ALREADY!")

    def borrowBook(self):
        pass

    def returnBook(self):
        pass