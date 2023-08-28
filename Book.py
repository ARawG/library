from Publisher import *
from BookType import *

class Book:
    def __init__(self, name:str, publisher:Publisher, book_type:BookType) -> None:
        self.name = name
        this.publisher = publisher
        this.book_type = book_type
        this.borrowed = False

    def get_info(self ) -> str:
        return (f"this book is: {this.name} \n from the publisher: {this.publisher.get_info()}")
    
    def return_book_type(self) -> BookType:
        return this.book_type