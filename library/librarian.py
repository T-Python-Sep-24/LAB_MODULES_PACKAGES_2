def add_book(library, title, author, isbn):
    if isbn in library:
        print(f"Book with ISBN {isbn} already exists.")
    else:
        library[isbn] = {'title': title, 'author': author, 'isbn': isbn, 'available': True}
        print(f"Added book: {title} by {author} (ISBN: {isbn})")

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
            print(f"Checked out book: {library[isbn]['title']} by {library[isbn]['author']}.")
        else:
            print(f"Book with ISBN {isbn} is already checked out.")
    else:
        print(f"No book found with ISBN {isbn}.")

def return_book(library, isbn):
    if isbn in library:
        library[isbn]['available'] = True
        print(f"Returned book: {library[isbn]['title']} by {library[isbn]['author']}.")
    else:
        print(f"No book found with ISBN {isbn}.")

def display_books(library):
    for book in library.values():
        status = "Available" if book['available'] else "Checked Out"
        print(f"{book['title']} by {book['author']} (ISBN: {book['isbn']}) - {status}")