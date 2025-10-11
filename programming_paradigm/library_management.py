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
        self._books = []   # ✅ تم تغييرها من __books إلى _books

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self , title):
        for book in self._books:
            if book.title == title:
                book.check_out()
                return
        print(f"Book {title} doesn't exist")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book.is_check_out():
                    print(f"The book '{title}' was not borrowed.")
                else:
                    book._is_checked_out = False   # مفضلش نلمسها، بس ما غيرتهاش حسب طلبك
                    print(f"The book '{title}' has been returned.")
                return
        print(f"Book '{title}' not found.")

    def list_available_books(self):
        for book in self._books:
            if book.is_check_out():
                print(f"{book.title} by {book.author}")
