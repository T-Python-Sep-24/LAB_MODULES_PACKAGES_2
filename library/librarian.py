def add_book(library, title, author, isbn):
    if isbn in library:
        print(f"Book with ISBN {isbn} already exists.")
    else:
        library[isbn] = {
            'title': title,
            'author': author,
            'isbn': isbn,
            'available': True
        }

def remove_book(library, isbn):
    if isbn in library:
        del library[isbn]
    else:
        print(f"No book found with ISBN {isbn}.")

def check_out_book(library, isbn):
    if isbn not in library:
        print(f"No book found with ISBN {isbn}.")
    elif not library[isbn]['available']:
        print(f"Book with ISBN {isbn} is already checked out.")
    else:
        library[isbn]['available'] = False

def return_book(library, isbn):
    if isbn not in library:
        print(f"No book found with ISBN {isbn}.")
    else:
        library[isbn]['available'] = True

def display_books(library):
    for book in library.values():
        status = "Available" if book['available'] else "Checked Out"
        print(f"{book['title']} by {book['author']} (ISBN: {book['isbn']}) - {status}")
