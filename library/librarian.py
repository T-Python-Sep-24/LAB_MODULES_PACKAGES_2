library = {}  

def add_book(library, title: str, author: str, isbn: str):
    if isbn in library:
        print("The book already exists.")
    else:
        library[isbn] = {
            "title": title,
            "author": author,
            "isbn": isbn,
            "available": True
        }
        print(f"Added {title} to library successfully.")

def remove_book(library, isbn: str):
    if isbn in library:
        del library[isbn]
        print("The book was deleted successfully.")
    else:
        print("Cannot find the book.")

def check_out_book(library, isbn: str):
    if isbn in library:
        if library[isbn]['available']:
            library[isbn]['available'] = False
            print(f"You have checked out the book: {library[isbn]['title']}.")
        else:
            print("The book is not available.")
    else:
        print("Cannot find the book.")

def return_book(library, isbn: str):
    if isbn in library:
        if not library[isbn]['available']:
            library[isbn]['available'] = True
            print(f"You have returned {library[isbn]['title']}.")
        else:
            print("The book is already available.")
    else:
        print("Cannot find the book.")

def display_books(library):
    if not library:
        print("The library is empty.")
    else:
        for isbn, details in library.items():
            print(f"{details['title']} by {details['author']}, ISBN: {isbn}, Available: {'Yes' if details['available'] else 'No'}")





