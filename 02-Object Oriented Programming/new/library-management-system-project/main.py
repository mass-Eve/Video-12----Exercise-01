from book_class import Book
from student_class import StudentID
from library_class import Library

# Instance of the main library
lib = Library()

# A student who want to borrow a book
student1 = StudentID()

# 4 books
book1 = Book()
book2 = Book()
book3 = Book()
book4 = Book()

lib.updateCatalogue(book1, book2, book3, book4)
lib.showCatalogue()