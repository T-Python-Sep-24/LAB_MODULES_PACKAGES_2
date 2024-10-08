from library import librarian

def main():
    library = {

    "9780316769174": {"title": "The Catcher in the Rye","author": "J.D. Salinger","isbn": "9780316769174","available": True},

    "9780446310789": {"title": "To Kill a Mockingbird","author": "Harper Lee", "isbn": "9780446310789","available": True },

    "9780451524935": { "title": "1984", "author": "George Orwell", "isbn": "9780451524935","available": True}
}

    while True:
        print(" 1 - add book")
        print(" 2 - remove book")
        print(" 3 - check out book")
        print(" 4 - return book")
        print(" 5 - display books")
        
        option = input("select an option 1 - 5 : " )

        if option == '1':
            title = str(input("enter book title : "))
            author = str(input("enter book author : "))
            isbn = str(input("enter book ISBN : "))
            librarian.add_book(library,title,author,isbn)

        elif option == '2':
            isbn = str(input("enter book ISBN : "))
            librarian.remove_book(library,isbn)

        elif option ==  '3':
            isbn = str(input(" enter book ISBN : "))
            librarian.check_out_book(library,isbn)

        elif option == '4':
            isbn = str(input("enter book ISBN : "))
            librarian.return_book(library,isbn)

        elif option == '5':
            librarian.display_books(library)

        else:

            print("invalid option")
        
main()