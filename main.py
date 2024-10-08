from library import librarian
library={}
isbn = 0
title= ""
author= ""
def main():
    while True:
        print("\n1. add a book")
        print("2. remove a book")
        print("3. check out a book")
        print("4. return a book")
        print("5. display books")
        print("6. Exit")

        choice = input("Select an option (1-6): ")

        if choice == '1':
            librarian.add_book(library,title,author,isbn)
        elif choice == '2':
            librarian.remove_book(library, isbn)
        elif choice == '3':
            librarian.check_out_book(library,isbn)
        elif choice == '4':
            librarian.return_book(library,isbn)
        elif choice == '5':
            librarian.display_books(library)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
while True:
    try:
        main()
        break
    except ValueError as e:
        print("please enter a valid number")