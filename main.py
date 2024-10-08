from library import librarian as lib
def display_menu():
    '''
    Displays the library menu options to the user.
    
    The function prints out a list of options that the user can choose from to 
    interact with the library system. The available options are:
    
    1 - Add a book
    2 - Remove a book
    3 - Check out a book
    4 - Return a book
    5 - Display all books
    0 - Exit
    
    The user will be prompted to enter a number corresponding to the action they want to perform.
    '''
    print("\nLibrary Menu:\n1 - Add a book\n2 - Remove a book\n3 - Check out a book\n4 - Return a book\n5 - Display all books\n0 - Exit")
    

def main():
    ''' 
         Runs the main library system interface for managing books.

    This function creates an empty library (a dictionary) and repeatedly
    presents the user with a menu of options to perform different actions 
    related to the library system. The user can:
    
    1. Add a book to the library
    2. Remove a book from the library
    3. Check out a book (mark it as unavailable)
    4. Return a book (mark it as available)
    5. Display all books in the library
    0. Exit the program
    
    The function continues to run until the user chooses to exit by entering 0.
    '''
    
    
    library = {}
    choice = -1 

    while choice != 0:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            t = input("Enter the book title: ")
            a = input("Enter the author: ")
            isbn = input("Enter the ISBN: ")
            lib.add_book(library, t, a, isbn)
            print(f"Book '{t}' added.")
        
        elif choice == 2:
            isbn = input("Enter the ISBN of the book to remove: ")
            lib.remove_book(library, isbn)
            print(f"Book with ISBN {isbn} removed (if it existed).")
        
        elif choice == 3:
            isbn = input("Enter the ISBN of the book to check out: ")
            lib.check_out_book(library, isbn)
        
        elif choice == 4:
            isbn = input("Enter the ISBN of the book to return: ")
            lib.return_book(library, isbn)
        
        elif choice == 5:
            print("\nLibrary collection:")
            lib.display_books(library)
        
        elif choice == 0:
            print("Exiting the library system. Goodbye!")
        
        else:
            print("Invalid choice. Please try again.")


main()
