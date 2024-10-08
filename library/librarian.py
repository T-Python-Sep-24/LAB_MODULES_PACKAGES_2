def add_book(library: dict, title: str, author: str, isbn: str):
    """ add book to library """
    print("\n------------- Adding a Book -------------")

    # loop through keys: then add book if not existed
    for isbnKey in library.keys():
        if isbnKey == isbn:
            print("============= Failed: ISBN is already existed =============")
            break
    else:
        newBookDict = {
            isbn: {
                "title": title,
                "author": author,
                "isbn": isbn,
                "available": True
            }
        }

        library.update(newBookDict)
        print(f"************* Book with ISBN: {isbn} was added successfully *************")
        input("")


def remove_book(library: dict, isbn: str):
    """ removes the book with the given ISBN from library """
    print("\n------------- Removing a Book -------------")

    for isbnKey in library.keys():
        if isbnKey == isbn:
            del library[isbnKey]
            print(f"************* The book with ISBN: {isbnKey} was removed successfully *************")
            input("")
            break
    else:
        print("============= Failed: ISBN does not exist =============")
        input("")
        

def check_out_book(library: dict, isbn: str):
    """ sets the 'available' key of the book with the given ISBN to False """
    print("\n------------- Checking Out a Book -------------")

    for isbnKey, value in library.items():
        if isbnKey == isbn:
            if value["available"] == True:
                value["available"] = False
                print(f"************* The book with ISBN: {isbnKey} was checked out successfully *************")
                input("")
            else:
                print("============= Failed: The book is not available =============")
                input("")
            break
    else:
        print("============= Failed: ISBN does not exist =============")
        input("")

def return_book(library: dict, isbn: str):
    """ sets the 'available' key of the book with the given ISBN to True """
    print("\n------------- Returning a Book -------------")

    for isbnKey, value in library.items():
        if isbnKey == isbn:
            if value["available"] == False:
                value["available"] = True
                print(f"************* The book with ISBN: {isbnKey} was returned successfully *************")
                input("")
            else:
                print("============= Failed: The book is already available =============")
                input("")    
            break
    else:
        print("============= Failed: ISBN does not exist =============")

def display_books(library: dict):
    """ prints all the books in the library """
    print("\n------------- Displaying the Books -------------")

    for isbnKey, value in library.items():
        availability: str = ""
        if value["available"] == True:
            availability = "Available"
        else:
            availability = "Checked Out"
    
        print(f"{value['title']} by : {value['author']} (ISBN: {isbnKey}) - {availability}")
    print("************* Displaying Books was completed successfully *************")
    input("")