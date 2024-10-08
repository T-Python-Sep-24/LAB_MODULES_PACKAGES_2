library={}
isbn = 0
title= ""
author= ""

def add_book(library, title:str, author:str, isbn:int):
    title = input("enter the title of the book: ")
    author= input("enter the author name of the book: ")
    isbn= int(input("enter the isbn of the book: "))
    if isbn in library:
        print(f"the book with isbn: {isbn} already exists.")
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
    isbn = int(input("Enter ISBN to delete: "))
    if isbn in  library:
        del library[isbn]
        print(f"book with isbn: {isbn} deleted.")
    else:
            print("the book is not here")



def check_out_book(library, isbn):
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
    if not library:
        print("no books")
    else:
        for isbn, book in library.items():
            print(f"{book['title']} by {book['author']} (ISBN: {book['isbn']}) - {'Available' if book['available'] else 'Checked Out'}")

     