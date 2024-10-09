# Function to add a book to the library
def add_book(library, title, author, isbn):
    # Check if the book already exists in the library
    if isbn in library:
        print(f"Book with ISBN {isbn} already exists.")
    else:
        # Add the new book with title, author, and availability status
        library[isbn] = {'title': title, 'author': author, 'available': True}
        print(f"Added: {title} by {author}")

# Function to remove a book from the library
def remove_book(library, isbn):
    # Check if the book exists
    if isbn in library:
        del library[isbn]  # Remove the book by ISBN
        print(f"Removed book with ISBN {isbn}.")
    else:
        print(f"No book found with ISBN {isbn}.")

# Function to check out a book (set it as unavailable)
def check_out_book(library, isbn):
    # Check if the book exists
    if isbn in library:
        if library[isbn]['available']:  # Check if the book is available
            library[isbn]['available'] = False  # Mark it as checked out
            print(f"Checked out: {library[isbn]['title']}")
        else:
            print(f"{library[isbn]['title']} is already checked out.")
    else:
        print(f"No book found with ISBN {isbn}.")

# Function to return a book (set it as available)
def return_book(library, isbn):
    # Check if the book exists
    if isbn in library:
        if not library[isbn]['available']:  # Check if it's checked out
            library[isbn]['available'] = True  # Mark it as returned
            print(f"Returned: {library[isbn]['title']}")
        else:
            print(f"{library[isbn]['title']} wasn't checked out.")
    else:
        print(f"No book found with ISBN {isbn}.")

# Function to display all books in the library
def display_books(library):
    # Loop through the books and print their details
    for isbn, book in library.items():
        status = "Available" if book['available'] else "Checked Out"
        print(f"{book['title']} by {book['author']} (ISBN: {isbn}) - {status}")
        
