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

def generate_report():
    if not library:
        print("no books fpund in library")
        return
    print("library report")
    print("-"*30)
    print("| ID | Title | Author | status |")
    print("-"*30)

    for book in library.values():
        status="borrowed" if book.is_borrowed else "available"
        print(f"| {book.book_id} | {book.title} | {book.author} | {status} |")


def menu():
    while True:
        print("\n Library Management System")
        print("1. Add Book \n2. Borrow book \n3. return book \n4. generate report \n5. exit")
        choice=input("enter your choice : ")
        if choice == "1":
            add_book()
        elif choice == "2":
            return_book()
        elif choice == "3":
            return_book()
        elif choice=="4":
            generate_report()
        elif choice == "5":
            print("exiting...")
            break
        else:
            print("invalid choice")




menu()
