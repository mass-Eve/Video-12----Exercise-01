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
        print("YOU ARE INSIDE CREATING A NEW BOOK")

        try:
            bname = input("Enter The Book Name :")
            self.book_name = bname

            ISBN = int(input("Enter The ISBN Number for the Book :"))

            price = int(input("Enter The Price Of The Book :"))
            self.selling_price = price

            writer = input("Enter The Name Of The Author Of The Book :")
            self.author = writer

            book_genre = input("Enter The Genre Of The Book :")
            self.genre = book_genre

            publish_year = int(input("Enter The Publishment Year Of The Book :"))
            self.pub_year = publish_year

            publication = input("Enter The Publication Publishing The Book :")
            self.publication_name = publication

            total_number_of_copies = int(input("Enter The Total Number Of Copies Of The Book Available In The Library :"))
            self.total_copies = total_number_of_copies

            self.quantities_available = total_number_of_copies

            print("New Book Added Successfully In The Catalog")

        except Exception as e:
            print(f'New Book Can Not Be Created Because Of The Following Error ~ {str(e)}')

    def displayBookDetails(self):

        try:
            print("----------------------------------------------------------------------------")
            print(f"BOOK NAME : {self.book_name}")
            print(f"AUTHOR NAME : {self.author}")
            print(f"PUBLICATION : {self.publication_name}")
            print(f"GENRE : {self.genre}")
            print(f"PUBLICATION YEAR : {self.pub_year}")
            print(f"ISBN : {self.isbn_number}")
            print(f"PRICE : {self.selling_price}")
            print(f"TOTAL COPIES AVAILABLE IN LIBRARY : {self.total_copies}")
            print(f"TOTAL COPIES AVAIABLE TO BORROW : {self.quantities_available}")
            print("----------------------------------------------------------------------------")
        except Exception as e:
            print(f'Book Details Can Not Be Fetched because of the following error ~ {str(e)}')

    def updateBookDetails(self):
        
        def menu():
            try:
                while(True):
                    # menu
                    print("-----------------------------------------------------------------------------------------")
                    print("\t\t\t\tWHAT WOULD YOU LIKE TO UPDATE ?")
                    print("1. ENTER 1 TO UPDATE BOOK NAME")
                    print("2. ENTER 2 TO UPDATE AUTHOR's NAME")
                    print("3. ENTER 3 TO UPDATE PUBLISHING HOUSE NAME")
                    print("4. ENTER 4 TO UPDATE GENRE OF THE BOOK")
                    print("5. ENTER 5 TO UPDATE THE PUBLISHING YEAR OF THE BOOK")
                    print("6. ENTER 6 TO UPDATE THE ISBN NUMBER OF THE BOOK")
                    print("7. ENTER 7 TO UPDATE THE SELLING PRICE OF THE BOOK")
                    print("8. ENTER 8 TO UPDATE THE TOTAL NUMBER OF COPIES OF THE BOOK AVAILABLE IN THE LIBRARY")
                    print("9. ENTER 9 TO UPDATE THE TOTAL NUMBER OF COPIES OF THE BOOK AVAILABLE TO BORROW")
                    print("10. ENTER 10 TO EXIT BOOK UPDATION MENU")
                    print("-----------------------------------------------------------------------------------------")

                    choice = int(input("What would you like to update ? : "))

                    match choice:
                        case 1:
                            updateName()
                        case 2:
                            updateAuthor()
                        case 3:
                            updatePublication()
                        case 4:
                            updateGenre()
                        case 5:
                            updateYear()
                        case 6:
                            updateISBN()
                        case 7:
                            updatePrice()
                        case 8:
                            updateTotalNoOfCopies()
                        case 9:
                            updateNoOfCopiesAvailableToBorrow()
                        case 10:
                            break
                        case _:
                            print("Check your input and try again later!")
            except Exception as e:
                print("------------------------------------------------------------------------------")
                print(f'book Details can not be updated because of the following error ~ {str(e)}')
                print("------------------------------------------------------------------------------")

        # update book name
        def updateName():
            try:
                print("------------------------------------------------------------------------------")
                newTitle = input("Enter the new title of the book : ")
                self.book_name = newTitle
                print("Book Title Updated Successfully........")
                print("------------------------------------------------------------------------------")
            except Exception as e:
                print("------------------------------------------------------------------------------")
                print(f"Book name can not be updated because of the following error ~ {str(e)}")
                print("------------------------------------------------------------------------------")

        # update author name
        def updateAuthor():
            try:
                print("------------------------------------------------------------------------------")
                newName = input("Enter the new author name : ")
                self.author = newName
                print("Author Name Updated Successfully........")
                print("------------------------------------------------------------------------------")
            except Exception as e:
                print("------------------------------------------------------------------------------")
                print(f"author name can not be updated because of the following error ~ {str(e)}")
                print("------------------------------------------------------------------------------")

        # update publication house name
        def updatePublication():
            try:
                print("------------------------------------------------------------------------------")
                newPub = input("Enter the new publication name : ")
                self.publication = newPub
                print("Publication Name Updated Successfully........")
                print("------------------------------------------------------------------------------")
            except Exception as e:
                print("------------------------------------------------------------------------------")
                print(f"Book Publication name can not be updated because of the following error ~ {str(e)}")
                print("------------------------------------------------------------------------------")

        # update genre of the book
        def updateGenre():
            try:
                print("------------------------------------------------------------------------------")
                newGenre = input("Enter the updated value for genre : ")
                self.genre = newGenre
                print("Book Genre Updated Successfully........")
                print("------------------------------------------------------------------------------")
            except Exception as e:
                print("------------------------------------------------------------------------------")
                print(f"Book genre can not be updated because of the following error ~ {str(e)}")
                print("------------------------------------------------------------------------------")

        # update the publishing year
        def updateYear():
            try:
                print("------------------------------------------------------------------------------")
                newYear = int(input("Enter the year of publishing : "))
                self.pub_year = newYear
                print("Publishing Year Updated Successfully........")
                print("------------------------------------------------------------------------------")
            except Exception as e:
                print("------------------------------------------------------------------------------")
                print(f"Book publishing year can not be updated because of the following error ~ {str(e)}")
                print("------------------------------------------------------------------------------")

        # update the ISBN Code of the book
        def updateISBN():
            try:
                print("------------------------------------------------------------------------------")
                newISBN = int(input("Enter the correct value of ISBN : "))
                self.isbn_number = newISBN
                print("Book ISBN Number Updated Successfully........")
                print("------------------------------------------------------------------------------")
            except Exception as e:
                print("------------------------------------------------------------------------------")
                print(f"Book ISBN details can not be updated because of the following error ~ {str(e)}")
                print("------------------------------------------------------------------------------")

        # update the selling price of the book
        def updatePrice():
            try:
                print("------------------------------------------------------------------------------")
                newPrice = int(input("Enter the new price of the book : "))
                self.price = newPrice
                print("Book Price Updated Successfully........")
                print("------------------------------------------------------------------------------")
            except Exception as e:
                print("------------------------------------------------------------------------------")
                print(f"Book Price can not be updated because of the following error ~ {str(e)}")
                print("------------------------------------------------------------------------------")

        # update total number of copies of the book
        def updateTotalNoOfCopies():
            try:
                print("------------------------------------------------------------------------------")
                total = int(input("Enter the updated number of total copies of this book : "))
                self.total_copies = total
                print("Book Capacity Updated Successfully........")
                print("------------------------------------------------------------------------------")
            except Exception as e:
                print("------------------------------------------------------------------------------")
                print(f"Book Capacity can not be updated because of the following error ~ {str(e)}")
                print("------------------------------------------------------------------------------")

        # update total number of copies of the book available for the people to borrow
        def updateNoOfCopiesAvailableToBorrow():
            try:
                print("------------------------------------------------------------------------------")
                total_available = int(input("Enter the total number of copies available to borrow : "))
                self.quantities_available = total_available
                print("Book Availability Updated Successfully........")
                print("------------------------------------------------------------------------------")
            except Exception as e:
                print("------------------------------------------------------------------------------")
                print(f"Book Availability can not be updated because of the following error ~ {str(e)}")
                print("------------------------------------------------------------------------------")

        # calling menu()
        menu()

    def checkAvaiablility(self):
        try:
            if (self.quantities_available > 0 and self.quantities_available <= self.total_copies):
                print("------------------------------------------------------------------------------")
                print(f'Total copies available to borrow are : {self.quantities_available}')
                print("YES YOU CAN BORROW THIS BOOK !")
                print("------------------------------------------------------------------------------")
                return True

            elif (self.quantities_available == 0):
                print("------------------------------------------------------------------------------")
                print(f'Total copies available to borrow are : {self.quantities_available}')
                print("NO YOU CAN NOT BORROW THIS BOOK, ALL THE COPIES ARE IN DISTRIBUTION ALREADY!")
                print("------------------------------------------------------------------------------")
                return False

            else:
                print("------------------------------------------------------------------------------")
                print("MANAGEMENT PROBLEM. PLEASE REPORT TO THE LIBRARIAN")
                print("------------------------------------------------------------------------------")
        except Exception as e:
            print("------------------------------------------------------------------------------")
            print("MANAGEMENT PROBLEM. PLEASE REPORT TO THE LIBRARIAN")
            print(str(e))
            print("------------------------------------------------------------------------------")

    def borrowBook(self):
        pass

    def returnBook(self):
        pass

one = Book()

# one.createBook()
# one.displayBookDetails()
# one.updateBookDetails()
# one.checkAvaiablility()