from library.librarian import add_book, remove_book, check_out_book, return_book, display_books

def main():
    library = {}

    # Adding books
    add_book(library, "The Catcher in the Rye", "J.D. Salinger", "9780316769174")
    add_book(library, "To Kill a Mockingbird", "Harper Lee", "9780446310789")
    add_book(library, "1984", "George Orwell", "9780451524935")

    # Display books
    print("\nBooks in Library:")
    display_books(library)

    # Check out a book
    print("\nChecking out 'The Catcher in the Rye':")
    check_out_book(library, "9780316769174")
    display_books(library)

    # Return a book
    print("\nReturning 'The Catcher in the Rye':")
    return_book(library, "9780316769174")
    display_books(library)

if __name__ == "__main__":
    main()