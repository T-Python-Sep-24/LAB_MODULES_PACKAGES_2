from library.librarian import *

def main():
    library={}
    add_book(library,"The Catcher in the Rye","J.D. Salinger" ,"9780316769174")
    add_book(library,"To Kill a Mockingbird","Harper Le" ,"9780446310789")
    add_book(library,"1984","George Orwel" ,"9780451524935")

    print("Initial Library :")
    display_books(library)

    print("\nChecking out 'The Catcher in The Rye':")
    check_out_book(library,"9780316769174")
    display_books(library)

    print("\nReturning 'The Catcher in The Rye':")
    return_book(library,"9780316769174")
    display_books(library)
    
    
    print("\nRemoving'1984':")
    remove_book(library, "9780451524935")
    display_books(library)

main()