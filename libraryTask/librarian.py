

def add_book(library, title, author, isbn):
    if isbn in library:
        print(f"Book with ISBN {isbn} already exists in the library.")
    else:
        library[isbn] = {
            'title': title,
            'author': author,
            'isbn': isbn,
            'available': True
        }
        print(f"Added book: {title} by {author} with ISBN {isbn}.")

def remove_book(library, isbn):
    if isbn in library:
        del library[isbn]
        print(f"Removed book with ISBN {isbn}.")
    else:
        print(f"No book found with ISBN {isbn}.")

def check_out_book(library, isbn):
    if isbn in library:
        if library[isbn]['available']:
            library[isbn]['available'] = False
            print(f"Checked out book with ISBN {isbn}.")
        else:
            print(f"Book with ISBN {isbn} is not available for checkout.")
    else:
        print(f"No book found with ISBN {isbn}.")

def return_book(library, isbn):
    if isbn in library:
        library[isbn]['available'] = True
        print(f"Returned book with ISBN {isbn}.")
    else:
        print(f"No book found with ISBN {isbn}.")

def display_books(library):
    if not library:
        print("No books in the library.")
        return
    
    for book in library.values():
        status = "Available" if book['available'] else "Checked Out"
        print(f"{book['title']} by {book['author']} (ISBN: {book['isbn']}) - {status}")