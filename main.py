#Importing the librarian module
import library.librarian as librarian

def main():
    '''
    Function that contains the main program operations
    '''
    library = {}
    print("Welcome to the Library System,", end = " ")
    while True:
        print("what would you like to do?")
        print("1. Add a book.\n2. Remove a book.\n3. Check out a book.\n4. Return a book.\n5. Display all books in the library.\n6. Exit.")
        #Store the librarian's choice 
        choice: str = input("Your choice: ")
        print("")
        if choice == '1':
            title: str = input("Enter the book's title: ")
            author: str = input("Enter the book's author: ")
            isbn: str = input("Enter the book's ISBN: ")
            librarian.add_book(library, title, author, isbn)
            input("")

        elif choice == '2':
            isbn: str = input("Enter the ISBN of the book you want to remove: ")
            librarian.remove_book(library, isbn)
            input("")

        elif choice == '3':
            isbn: str = input("Enter the ISBN of the book you want to check out: ")
            librarian.check_out_book(library, isbn)
            input("")

        elif choice == '4':
            isbn: str = input("Enter the ISBN of the book you want to retun: ")
            librarian.return_book(library, isbn)
            input("")

        elif choice == '5':
            print("Fetching library data..")
            librarian.display_books(library)
            input("")
            
        elif choice == '6':
            print("Existing library system..")
            break
        else:
            print("Invalid choice, try again.")
            input("")

#Calling the main function and starting execution
main()