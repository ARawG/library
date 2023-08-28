from Book import *
class Library:
    def __init__(self, name:str, location:str, books:list) -> None:
        this.name = name
        this.location = location
        this.books = books

    def add_book(self, book:Book):
        this.books.append(book)

    def remove_book(Self, book:Book):
        this.books.remove(book)

    def search_book(self, book:Book) -> bool:
        if book in this.books:
            return True
        else:
            return False
        
    def return_book_by_type(self, book_type:BookType):
        books = []
        for book in this.books:
            if this.book.return_book_type() == book_type :
                books.append(book)
        return books        