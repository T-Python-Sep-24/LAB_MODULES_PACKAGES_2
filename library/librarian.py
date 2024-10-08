# Sample of books dictionary
# library{
#   "9780316769174": {
#       "title": "The Catcher in the Rye",
#       "author": "J.D. Salinger",
#       "available": True
#   }
# }


# Add Book Function
def add_book(library: dict, title: str, author: str, isbn: str):
    """
        a function to add a book to the library's dictionary
    :args
        library:
        title:
        author:
        isbn:
    :return: None
    """
    if isbn not in library:
        library[isbn] = {

            "title": title,
            "author": author,
            "available": True

        }
        print(f"The Book \"{library[isbn]["title"]}\" is added successfully")
    else:
        print("Book is already added")


# Remove Book Function
def remove_book(library: dict, isbn:str):
    """
    a function to remove a book from the library's dictionary
    :Args
        library:
        isbn:
    :return: None
    """

    if isbn in library:
        bookTitle = library[isbn]["title"]
        conf = input(f"Are You sure you want to delete \"{bookTitle}\" [Y/N]")
        if conf.lower() == "y":
            del library[isbn]
            print(f"The book \"{bookTitle}\" is deleted Successfully")

    else:
        print("The book was not found")


# Check out Books Function
def check_out_book(library, isbn):

    if isbn in library:
        if library[isbn]["available"]:
            library[isbn]["available"] = False
            print(f"\"{library[isbn]["title"]}\" is Checked Out for you Successfully")
        else:
            print("Sorry, The book you're looking for is not available at the moment, try again soon")
    else:
        print("The Book your are looking for is not in our library")


# Return Books Function
def return_book(library, isbn):

    if isbn in library and not library[isbn]["available"]:
        library[isbn]["available"] = True
        print("Thank You, Please Keep Reading and Learning")
        print(f"Returning Book... \"{library[isbn]["title"]}\"")

    elif isbn in library and library[isbn]["available"]:
        print("The Book is Already Returned")

    else:
        print("The Book your are trying to return is not in our library")


# Print All Books Function
def display_books(library):
    if len(library) >= 1:
        print("")
        for i, bookReference in enumerate(library, start=1):
            availability = "Checked Out"
            if library[bookReference]["available"]:
                availability = "Available"
            print(f"{i}. {library[bookReference]["title"]} Authored By: {library[bookReference]["author"]} (ISBN NO: {bookReference}) - {availability}")
        print("")
            # print(library[bookReference])
            # library[isbn]["title"]

    else:
        print("Library is Empty now, come again later.")