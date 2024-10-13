

from librarian import add_book, remove_book, check_out_book, return_book, display_books

def main():
    library = {}

    add_book(library, "The Catcher in the Rye", "J.D. Salinger", "9780316769174")
    add_book(library, "To Kill a Mockingbird", "Harper Lee", "9780446310789")
    add_book(library, "1984", "George Orwell", "9780451524935")


    display_books(library)
    print()  

    check_out_book(library, "9780316769174")
    display_books(library)
    print() 


    return_book(library, "9780316769174")
    display_books(library)

if __name__ == "__main__":
    main()