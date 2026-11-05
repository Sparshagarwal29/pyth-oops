#  PRACTICE 
# QUESTION 
# You are asked to model a real-world system with four core components:
# Book (Base Class): Serves as the parent class containing shared properties like title, author, and ISBN.
# DigitalBook & PhysicalBook (Subclasses): Inherit from Book. They add format-specific features (e.g., file size for digital books, shelf location for physical books).

# Member & Library: Member represents a person borrowing books, while Library manages the overall collection of books and registered members.

# __eq__ Dunder Method: Customizes equality so two Book objects are considered equal (book1 == book2) if they share the same ISBN, even if they are two separate objects created in memory.

# Borrow Session (Context Manager): Implements __enter__ and __exit__ to manage borrowing using Python's with statement.

# When you enter the with block (__enter__), the book is checked out to the member.

# When exiting the with block (__exit__), the book is automatically returned to the library—even if an error occurs inside the block.44



class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
    def __eq__(self, other): 
        return self.ISBN == other.ISBN
    def __repr__(self):
        return f"Book{self.title}, author{self.author}"


class DigitalBook(Book):
    def __init__(self, title, author, ISBN,file_size):
        super().__init__(title, author, ISBN)
        self.file_size = file_size

class PhysicalBook(Book):
    def __init__(self,title,author,ISBN,shelf_loc):
        super().__init__(title,author,ISBN)
        self.shelf_loc=shelf_loc

class Member:
    def __init__(self,member_id,name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = [] 
    def __repr__(self):
        return f"Member(name='{self.name}', id='{self.member_id}')"


class Libary:
    def __init__(self,name):
        self.name = name
        self.books = []  #this iw what we call compostion 
        self.members = [] #this is what we call composition

    def add_book(self,book: Book):
        self.books.append(book)

    def iss_book_availbale(self,book: Book):
        return book in self.books
        

    def registered_member(self,member: Member):
        self.members.append(member)


# this borrowsession act as a context manager 
# context manger have 3 function __init__ , __enter__ , __exit__ 
class BorrowSession:
    def __init__(self,library:Libary,member:Member,book:Book):
        self.library= library
        self.member = member
        self.book = book

    def __enter__(self):
        if not self.library.iss_book_availbale(self.book):
            return f"{self.book.title} by author{self.book.author} does not exit in {self.library.name}"
        self.library.books.remove(self.book)
        self.member.borrowed_books.append(self.book)
        print(f"-> [BORROWED] '{self.book.title}' checked out to {self.member.name}.")
        return self.book
# exc_type	Exception class/type
# exc_val	Exception object containing the error details
# exc_tb	Traceback information (where the error occurred)
    def __exit__(self, exc_type, exc_val, tb):
        if self.book in self.member.borrowed_books:
            self.member.borrowed_books.remove(self.book)
            self.library.add_book(self.book)
        if exc_type:
            print (f"an error occur inside{exc_val}")
        return False
