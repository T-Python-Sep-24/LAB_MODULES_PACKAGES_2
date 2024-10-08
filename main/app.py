from library.librarian import *

# main method
def app():
    """
        This is the main function that interacts with user and call the
        appropriate methods according to user choice.

    """
    # Sample of books dictionary
    # library[111] = {
    #     "title": JAVA,
    #     "author": don't know,
    #     "isbn": 111,
    #     "available": True
    # }
    bookleeList = {

        "111": {
            "title": "JAVA",
            "author": "don't know",
            "isbn": "111",
            "available": True
        },
        "222": {
            "title": "Python Principles",
            "author": "don't know",
            "isbn": "222",
            "available": False
        }

    }
    while True:
        try:

            print("-"*8, "Welcome to Booklee", "-"*8)
            print(" 1. Display Books "
                  "\n 2. check out a book "
                  "\n 3. return a book "
                  "\n 4. add a book "
                  "\n 5. remove a book "
                  "\n Q/q Quit application")
            print("-"*36)
            choice = input(">>> Enter Your Choice: ")

            if choice == "1":
                # display books method
                display_books(bookleeList)
                input(" > To show the list please press any button < ")

            elif choice == "2":
                # checking out a book
                isbn = input("Enter ISBN number: ")
                check_out_book(bookleeList, isbn)
                input(" > To show the list please press any button < ")

            elif choice == "3":
                # returning a book
                isbn = input("Enter ISBN number: ")
                return_book(bookleeList, isbn)
                input(" > To show the list please press any button < ")

            elif choice == "4":
                # Adding a new book
                title: str = input("Enter Book Title: ")
                author: str = input("Enter Book Author Name: ")
                isbn: int = int(input("Enter ISBN number: "))
                add_book(bookleeList, title, author, str(isbn))
                input(" > To show the list please press any button < ")

            elif choice == "5":
                # removing a book
                isbn = input("Enter ISBN number: ")
                remove_book(bookleeList, isbn)
                input(" > To show the list please press any button < ")

            elif choice.lower() == "q":
                # Exit
                print("Thank You For Using \"Booklee\", See Your Later")
                break

            else:
                # wrong inputs
                print("Please Enter a valid choice from the list.")

        except ValueError:
            print("Please Enter Valid Data")


# starting the application

app()
