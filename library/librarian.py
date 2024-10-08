

def add_book(library:dict, title :str, author:str, isbn :str):
    ''''
         Adds a book to the library.

    If the book's ISBN is not already in the library, adds a new entry with
    the book's title, author, and sets the availability to True.

    Args:
        library (dict): The dictionary representing the library.
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The ISBN of the book.
    '''

    if isbn not in library :
        library[isbn] = {
            "title": title,
            "author": author,
            "available": True
        }
    else:
        print("book is already exist!")    

def remove_book(library, isbn):
    '''
        Removes a book from the library.

    If the book with the given ISBN exists, it will be removed from the library.
    If the book does not exist, nothing happens.

    Args:
        library (dict): The dictionary representing the library.
        isbn (str): The ISBN of the book to be removed.
    '''

    library.pop(isbn, "Book is not fount")

def check_out_book(library, isbn):
    '''
    Checks out a book from the library.

    If the book is available, it sets the 'available' status to False.
    If the book is already checked out or not found, prints an error message.

    Args:
        library (dict): The dictionary representing the library.
        isbn (str): The ISBN of the book to be checked out.
    '''
    
    if library.get(isbn) and library[isbn]['available']:
        library[isbn]['available'] = False
    else:
        print(f"Cannot check out book with ISBN {isbn}.")

def return_book(library, isbn):
    
    '''
     Returns a book to the library.

    If the book was checked out, its 'available' status will be set to True.
    If the book is already available or does not exist, prints an appropriate message.

    Args:
        library (dict): The dictionary representing the library.
        isbn (str): The ISBN of the book to be returned.
    '''
    
    if library.get(isbn):
        if not library[isbn]['available']:
            library[isbn]['available'] = True
            print(f"Book with ISBN {isbn} has been returned.")
        else:
            print(f"Book with ISBN {isbn} is already in library (Not checked out).")
    else:
        print(f"Book with ISBN {isbn} not found.")

def display_books(library):
    if not library:
        print("No books available in the library.")
        return

    for isbn, book in library.items():
        status = 'Available' if book['available'] else 'Checked Out'
        print(f"{book['title']} by {book['author']} (ISBN: {isbn}) - {status}")




