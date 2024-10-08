
def add_book(library, title: str, author: str, isbn: str):
    '''
    This function adds a new book as dictionary to the library dictionary (nested dict) 
    Args:
        library (dict): A dictionary that contains all books in the library
        title (str): The title of the book
        author (str): The author of the book
        isbn (str): The unique id of the book

    Return:
        none    
    '''
    if isbn in library:
        print(f"A book with an ISBN of {isbn} already exists in the library.")
    else:
        library[isbn] = {
            'title': title,
            'author': author,
            'isbn': isbn,
            'available': True
        }
        print("Book has been successfully added.")

def remove_book(library, isbn: str):
    '''
    This function removes a book from library dictionary if it exists
    Args:
        library (dict): A dictionary that contains all books in the library
        isbn (str): The unique id of the book
    Return:
        none
    '''
    if isbn in library:
        del library[isbn]
        print("Book has been successfully removed.")
    else:
        print("The book doesn't exist in the library.")

def check_out_book(library, isbn: str):
    '''
    This function marks a book's availability to False if its ISBN exists
    Args:
        library (dict): A dictionary that contains all books in the library
        isbn (str): The unique id of the book
    Return:
        none
    '''
    if isbn in library:
        if library[isbn]['available'] != False:
            library[isbn]['available'] = False
            print(f"The book '{library[isbn]['title']}' has been checked out.")
        else:
            print(f"Sorry, the book {library[isbn]['title']} is unavailable.")
    else:
        print("The book doesn't exist in the library.")

def return_book(library, isbn: str):
    '''
    This function marks a book's availability to True if its ISBN exists
    Args:
        library (dict): A dictionary that contains all books in the library
        isbn (str): The unique id of the book
    Return:
        none
    '''
    if isbn in library:
        #Make sure the book isn't already available 
        if library[isbn]['available'] != True:
            library[isbn]['available'] = True
            print(f"The book '{library[isbn]['title']}' has been returned to the library.")
        else:
            print(f"The book {library[isbn]['title']} is not checked out.")
    else:
        print("The book doesn't exist in the library.")

def display_books(library):
    '''
    This function prints the information of books in a given library if any
    '''
    availability:str
    #Checking that the library dict isn't empty
    if library:
        for i, isbn in enumerate(library):
            if library[isbn]['available'] == True:
                availability = "Available"
            else:
                availability = "Checked out"
            
            print(f"{i + 1}. {library[isbn]['title']} by {library[isbn]['author']} ISBN: {isbn} - {availability}\n")
    else:
        print("The library has no books to display.")
