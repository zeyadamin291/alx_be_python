
'''
Implement a Library class with a private list _books to store instances of Book.
Include methods to add_book, check_out_book(title), return_book(title), and list_available_books.
'''

class Book:
    def __init__(self , title , author):
        self.title = title
        self.author = author
        self.__is_checked_out = False 
    
    def check_out(self):
        if self.__is_checked_out:
            print(f"the book {self.title} is already borrowed")
        else:
            print(f"the book {self.title} has been borrowed")
            self.__is_checked_out = True
    def is_check_out(self):
        return self.__is_checked_out 
    
    def return_book(self):
        if not self.__is_checked_out:
            print(f"the book {self.title} was not borrowed")
        else:
            print(f"the book {self.title} has been returned")
            self.__is_checked_out = False
        

class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)

    def check_out_book(self , title):
        for book in self.__books:
            if book.title == title:
                book.check_out()
                return
        print(f"Book {title} doesn't exist")

    def return_book(self, title):
        for book in self.__books:
            if book.title == title:
                if not book.is_check_out():
                    print(f"The book '{title}' was not borrowed.")
                else:
                    book._is_checked_out = False
                    print(f"The book '{title}' has been returned.")
                return
        print(f"Book '{title}' not found.")


    def list_available_books(self):
        for book in self.__books:
            if book.is_check_out():
                print(f"{book.title} by {book.author}")




# def main():
#     # Setup a small library
#     library = Library()
#     library.add_book(Book("Brave New World", "Aldous Huxley"))
#     library.add_book(Book("1984", "George Orwell"))

#     # Initial list of available books
#     print("Available books after setup:")
#     library.list_available_books()

#     # Simulate checking out a book
#     library.check_out_book("1984")
#     print("\nAvailable books after checking out '1984':")
#     library.list_available_books()

#     # Simulate returning a book
#     library.return_book("1984")
#     print("\nAvailable books after returning '1984':")
#     library.list_available_books()

# if __name__ == "__main__":
#     main()