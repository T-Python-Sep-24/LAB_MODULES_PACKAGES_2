library={}
isbn = 0
title= ""
author= ""

def add_book(library, title:str, author:str, isbn:int):
    """
    this function is used to add a book to the library
    """
    title = input("enter the title of the book: ")
    author= input("enter the author name of the book: ")
    isbn= int(input("enter the isbn of the book: "))
    if isbn in library:
        print(f"the book with ISBN: {isbn} already exists.")
    else:
        library[isbn]= {}
        library[isbn] ={
            'title': title,
            'author': author,
            'isbn': isbn,
            'available': True
        }
        print(f"The book '{title}' by {author} has been added to the library.")





def remove_book(library, isbn):
    """
    this function is used to remove a book from the library
    """
    isbn = int(input("Enter ISBN of the book you want to remove: "))
    if isbn in  library:
        del library[isbn]
        print(f"book with isbn: {isbn} removed.")
    else:
            print("the book is not here")



def check_out_book(library, isbn):
    """
    this function is used to check out a book from the library
    """
    isbn = int(input("Enter ISBN of the book you want to check out: "))
    if isbn in  library:

        if library[isbn]['available']:
            library[isbn]['available'] = False
            
            print(f"The book '{library[isbn]['title']}' has been checked out.")
        else:
             print("the book is not available")
    else:
            print("the book is not here")



def return_book(library, isbn):
    """
    this function is used to return a book to the library
    """
    isbn = int(input("Enter ISBN of the book you want to return: "))
    if isbn in  library:

        if library[isbn]['available'] == False:
            library[isbn]['available'] = True
            print(f"The book '{library[isbn]['title']}' has been returned.")
        else:
             print("the book is already returned")
    else:
            print("the book is not here")



def display_books(library):
    """
    this function is used to display all books in the library
    """
    if not library:
        print("no books")
    else:
        for isbn, book in library.items():
            print(f"{book['title']} by {book['author']} (ISBN: {book['isbn']}) - {'Available' if book['available'] else 'Checked Out'}")

     