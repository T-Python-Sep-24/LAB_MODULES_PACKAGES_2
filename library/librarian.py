def add_book(library, title, author, isbn):
    if isbn in library:
        print(f"Book with ISBN {isbn} already exists.")
    else:
        library[isbn] = {'title': title, 'author': author, 'available': True}

def remove_book(library, isbn):
    if isbn in library:
        del library[isbn]
    else:
        print(f"Book with ISBN {isbn} not found.")

def check_out_book(library, isbn):
    if isbn in library:
        if library[isbn]['available']:
            library[isbn]['available'] = False
        else:
            print(f"Book '{library[isbn]['title']}' is already checked out.")
    else:
        print(f"Book with ISBN {isbn} not found.")

def return_book(library, isbn):
    if isbn in library:
        if not library[isbn]['available']:
            library[isbn]['available'] = True
        else:
            print(f"Book '{library[isbn]['title']}' is already available.")
    else:
        print(f"Book with ISBN {isbn} not found.")

def display_books(library):
    for isbn, book in library.items():
        status = 'Available' if book['available'] else 'Checked Out'
        print(f"{book['title']} by {book['author']} (ISBN: {isbn}) - {status}")
