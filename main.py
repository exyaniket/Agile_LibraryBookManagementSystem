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

def borrow_book():
    book_id=int(input("enter book id to borrow : "))
    if book_id not in library:
        print("book not found")
        return
    
    library[book_id].is_borrowed=True
    print("book borrowed successfully")

def return_book():
    book_id=int(input("enter bookid to return : "))
    if book_id not in library:
        print("book record not found")
        return
    
    if not library[book_id].is_borrowed:
        print("book not borrowed!!")
        return
    library[book_id].is_borrowed=False
    print("book returned successfully")

add_book()
borrow_book()
return_book()