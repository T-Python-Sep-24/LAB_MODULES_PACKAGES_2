from library.librarian import *

# main method
def app():
    """
        This is the main function that interacts with user and call the
        appropriate methods according to user choice.

    """
    # Sample of books dictionary
    # library{
    #   "9780316769174": {
    #       "title": "The Catcher in the Rye",
    #       "author": "J.D. Salinger",
    #       "available": True
    #   }
    # }
    bookleeList = {

        "9781451628425": {
            "title": "A Beautiful Mind",
            "author": "Sylvia Nasar",
            "available": True
        },
        "9780393866667": {
            "title": "A Hacker's Mind",
            "author": "Bruce Schneier",
            "available": True
        },
        "9780078022128": {
            "title": "Software Engineering A Practitioner's Approach",
            "author": "Roger S. Pressman",
            "available": True
        },

    }
    while True:
        print("")
        try:

            print("-"*8, "Welcome to Booklee", "-"*8)
            print(" 1. Display Books "
                  "\n 2. check out a book "
                  "\n 3. return a book "
                  "\n 4. add a book "
                  "\n 5. remove a book "
                  "\n Q/q Quit application")
            print("-"*36)
            choice = input(" >>> Enter Your Choice: ")

            if choice == "1":
                # display books method
                display_books(bookleeList)
                input(" > To show the list please press any button < ")

            elif choice == "2":
                # checking out a book
                isbn: int = int(input(" >> Enter ISBN number to Check out book: "))
                check_out_book(bookleeList, str(isbn))
                input(" > To show the list please press any button < ")

            elif choice == "3":
                # returning a book
                isbn: int = int(input(" >> Enter ISBN number return book: "))
                return_book(bookleeList, str(isbn))
                input(" > To show the list please press any button < ")

            elif choice == "4":
                # Adding a new book
                title: str = input(" >> Enter Book Title: ")
                author: str = input(" >> Enter Book Author Name: ")
                isbn: int = int(input(" >> Enter Book ISBN number: "))
                add_book(bookleeList, title, author, str(isbn))
                input(" > To show the list please press any button < ")

            elif choice == "5":
                # removing a book
                isbn: int = int(input(" >> Enter ISBN number to remove book: "))
                remove_book(bookleeList, str(isbn))
                input(" > To show the list please press any button < ")

            elif choice.lower() == "q":
                # Exit
                print("Thank You For Using \"Booklee\", See Your Later")
                break

            else:
                # wrong inputs
                print("Please Enter a valid choice from the list.")

        except ValueError:
            print("Incorrect Entry, Please Enter Valid Information")


# starting the application

app()
