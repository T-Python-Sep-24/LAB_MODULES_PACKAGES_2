# Sample of books dictionary
# library[111] = {
#     "title": JAVA,
#     "author": don't know,
#     "isbn": 111,
#     "available": True
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
            "isbn": isbn,
            "available": True
        }
        print(f"The Book {library[isbn]["title"]} is added successfully")
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
        conf = input(f"Are You sure you want to delete {library[isbn]["title"]} [Y/N]")
        if conf.lower() == "y":
            del library[isbn]
            print("Book is deleted Successfully")

    else:
        print(f"{isbn} was not found")

# Check out Books Function
def check_out_book(library, isbn):

    if isbn in library:
        if library[isbn]["available"]:
            library[isbn]["available"] = False
            print(f"{library[isbn]["title"]} is Checked Out for you Successfully")
        else:
            print("Sorry, The book you're looking for is not available at the moment, try again soon")
    else:
        print("The Book your are looking for is not in our library")

# Return Books Function
def return_book(library, isbn):

    if isbn in library:
        library[isbn]["available"] = True
        print("Thank You, Please Keep Reading and Learning")
        print("Returning Book...")
    else:
        print("The Book your are trying to return is not in our library")

# Print All Books Function
def display_books(library):
    if len(library) >= 1:
        for i, book in enumerate(library, start=1):
            print(f"{i}. {library[book]["title"]} Authored By: {library[book]["author"]} ISBN NO: {library[book]["isbn"]}, Availability: {library[book]["available"]}")
            # print(library[book])
            # library[isbn]["title"]

    else:
        print("Library is Empty now, come again later.")