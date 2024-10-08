from library.librarian import add_book, remove_book, check_out_book, return_book, display_books

def main():
    library = {}

    # Adding books
    add_book(library, "The Catcher in the Rye", "J.D. Salinger", "9780316769174")
    add_book(library, "To Kill a Mockingbird", "Harper Lee", "9780446310789")
    add_book(library, "1984", "George Orwell", "9780451524935")

    # Displaying books
    print("Initial library:")
    display_books(library)
    print()

    # Checking out a book
    check_out_book(library, "9780316769174")
    print("After checking out 'The Catcher in the Rye':")
    display_books(library)
    print()

    # Returning a book
    return_book(library, "9780316769174")
    print("After returning 'The Catcher in the Rye':")
    display_books(library)
    print()

    # Removing a book
    remove_book(library, "9780446310789")
    print("After removing 'To Kill a Mockingbird':")
    display_books(library)

if __name__ == "__main__":
    main()