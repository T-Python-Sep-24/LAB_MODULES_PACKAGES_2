def add_book(library, title, author, isbn):
    if isbn in library:
        print("exist") 
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
        print(f"Book with ISBN {isbn} has been removed.")
    else:
        print(f"No book found with ISBN {isbn}.")

def return_book(library, isbn):
    if isbn in library:
        library[isbn]['available'] = True
        print(f"You have returned '{library[isbn]['title']}' by {library[isbn]['author']}.")
    else:
        print(f"No book found with ISBN {isbn}.")        

def display_books(library):
    if not library:
        print("No books in the library.")
    else:
        for isbn, book in library.items():
            availability = "Available" if book['available'] else "Not Available"
            print(f"ISBN: {isbn}, Title: '{book['title']}', Author: {book['author']}, Status: {availability}")

library = {}
add_book(library, "1984", "George Orwell", "1234567890")
add_book(library, "To Kill a Mockingbird", "Harper Lee", "0987654321")
display_books(library)
