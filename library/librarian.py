
def add_book(library:dict, title:str, author:str, isbn:str):
    '''
    The function adds the book information to the dictionary
    Args:
        library(dict): the dictionary to add information
        title (srt): the title of the book
        author(str):the author of the book
        isbn(str): the international Standard Book Number 
    Returns:
        None
    '''
    
    library[isbn]={
            'title':title,
            'author':author,
            'isbn':isbn,
            'available':True
        }
    print(f"a Book with the title : {title} by {author} was added to the library")
    
    

def remove_book(library:dict, isbn:str):
    '''
    The function deletes book
    Args:
        library(dict): the library that saves books
        isbn(str):The key to the dictinory
    Returns:
        None
    '''
    del library[isbn]
    print("the book has been deleted")

def check_out_book(library:dict, isbn:str):
    """
    The function allow the user to borrow a book from the library
    Args:
        library(dict):the library that holds book
        isbn(str):the key to the library
    Returns:
        None
        
    """
    library[isbn]['available']=False
    print("Don't forget to Bring it back!")

def return_book(library, isbn):
    """
    The function is when the user returns the borrowed book
    Args:
        library(dict):the library that holds book
        isbn(str):the key to the library
    Returns:
        None

    """
    library[isbn]['available']=True

def display_books(library:dict):
    """
    The function displays what books inside the library
    Args:
        library(dict):the library
    Returns:
        None
    """
    for book in library.values():
        availability="Avalible"if book['available'] else "Checked Out"
        print(f"The {book['title']} by {book['author']} (ISBN: {book['isbn']}) -{availability}")

        

