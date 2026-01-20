class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

library = {}

def add_book():
    book_id=int(input("enter book id : "))
    if book_id in library:
        print("error : duplicate book !")
        return
    
    title=input("enter title : ")
    author=input("enter author: ")

    library[book_id]=Book(book_id,title,author)
    print("book added successfully");
