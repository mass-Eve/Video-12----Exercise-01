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

    def updateBookDetails(self):
        
        # update book name
        def updateName(self):
            newTitle = input("Enter the new title of the book : ")
            self.book_name = newTitle
            print("Book Title Updated Successfully........")

        # update author name
        def updateAuthor(self):
            newName = input("Enter the new author name : ")
            self.author = newName

        # update publication house name
        def updatePublication(self):
            newPub = input("Enter the new publication name : ")
            self.publication = newPub

        # update genre of the book
        def updateGenre(self):
            newGenre = input("Enter the updated value for genre : ")
            self.genre = newGenre

        # update the publishing year
        def updateYear(self):
            newYear = int(input("Enter the year of publishing : "))
            self.pub_year = newYear

        # update the ISBN Code of the book
        def updateISBN(self):
            newISBN = int(input("Enter the correct value of ISBN : "))
            SELF.isbn_number = newISBN

        # update the selling price of the book
        def updatePrice(self):
            newPrice = int(input("Enter the new price of the book : "))
            self.price = newPrice

        # update total number of copies of the book
        def updateTotalNoOfCopies(self):
            total = int(input("Enter the updated number of total copies of this book : "))
            self.total_copies = total

        # update total number of copies of the book available for the people to borrow
        def updateNoOfCopiesAvailableToBorrow(self):
            total_available = int(input("Enter the total number of copies available to borrow : "))
            self.quantities_available = total_available

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