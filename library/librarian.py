def add_book(library:dict, title:str, author:str, isbn:str):
    if isbn in library:
        print("Book with ISBN{isbn}already exists in the libary")
    else:
        library[isbn]={"title":title,"author":author,'available':True}

def remove_book(library:dict, isbn:str):
    if isbn in library:
        del library[isbn]
    else:
        print("Book with ISBN{isbn}does not exists in the libary")

def check_out_book(library:dict, isbn:str):
    if isbn in library:
        if library[isbn]['available']:
            library[isbn]['available']=False
        else:
            print("Book with ISBN{isbn}is already checked out")
    else:
        print("Book with ISBN{isbn}does not exists in the libary")

def return_book(library:dict, isbn:str):
    if isbn in library:
        library[isbn]['available']=True
    else:
        print("Book with ISBN{isbn}does not exists in the libary")

def display_books(library:dict):
    for isbn, book in library.items():
        availability="Available" 
        if book ['available']== True :
            availability="Available"
        else:
            availability="Checked Out"
        print(f"{book['title']} by {book['author']}(ISBN:{isbn})- {availability}")

            