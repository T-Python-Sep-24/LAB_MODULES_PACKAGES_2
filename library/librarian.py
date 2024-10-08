library={}
def add_book(library,title, author, isbn):
    if isbn in library:
        print("the isbn already exists in the library")
        return
    library[isbn]={
        'title': title,
        'author': author,
        'isbn': isbn,
        'available': True
    }
    print(f"book {title} by {author} added successfully")

def remove_book(library, isbn):
    if isbn not in library:
        print(f"book with isbn {isbn} does not exist")
        return
    del library[isbn]
    print(f"book with isbn {isbn} removed")

def check_out_book(library, isbn):
    if isbn not in library:
        print(f"book with isbn {isbn} does not exist")
        return
    if not library[isbn]["available"]:
        print(f"book with isbn {isbn} not available")
        return
    library[isbn]["available"]=False
    print(f"book with isbn {isbn} checked out")

def return_book(library,isbn):
    if isbn not in library:
        print(f"the book with isbn {isbn} not exist")
        return
    library[isbn]["available"]=True
    print(f"book with isbn {isbn} has returned")

def display_books(library):
    if not library:
        print("no book found")
        return
    for book in library.values():
        if book["available"]:
            availability="available"
        else:
            availability ="checked out"
        print(f"{book['title']} by {book['author']} (isbn: {book['isbn']}) - {availability}")