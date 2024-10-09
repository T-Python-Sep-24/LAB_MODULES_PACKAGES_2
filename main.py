from library import librarian

def main():
    # Create an empty library dictionary
    library = {}

    # Add some books to the library
    librarian.add_book(library, "The Catcher in the Rye", "J.D. Salinger", "9780316769174")
    librarian.add_book(library, "To Kill a Mockingbird", "Harper Lee", "9780446310789")
    librarian.add_book(library, "1984", "George Orwell", "9780451524935")

    # Display the books in the library
    print("\nBooks in the library:")
    librarian.display_books(library)

    # Check out a book
    librarian.check_out_book(library, "9780316769174")
    print("\nAfter checking out 'The Catcher in the Rye':")
    librarian.display_books(library)

    # Return the book
    librarian.return_book(library, "9780316769174")
    print("\nAfter returning 'The Catcher in the Rye':")
    librarian.display_books(library)

if __name__ == "__main__":
    main()
