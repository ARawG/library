from Book import *

class Member:
    def __init__(self, id:int, name:str) -> None:
        this.id = id
        this.name = name
        this.books = []

    def add_book(self, book:Book):
        this.books.append(book)
    
    def borrowed_book_count(self):
        return len(this.books)
    
    def is_borrowed_book(self, book:Book):
        if book in this.books:
            return True
        else:
            return False