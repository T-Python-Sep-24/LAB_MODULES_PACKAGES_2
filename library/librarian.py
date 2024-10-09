
def add_book(library, title, author, isbn):
    if isbn in library:
        print("Available")
    library[isbn]={
        "title":title,
        "author":author,
        'isbn':isbn,
        "available":True
    }
    print(f"added")
def remove_book(library, isbn):
    if isbn in library:
        del library[isbn]
        print(f"{isbn} has been removed")
    else:
        print("this Book is not available")
def check_out_book(library, isbn):
    if library[isbn]["available"]:
        library[isbn]["available"] = False
        print(f"{isbn} has been Check out")



def return_book(library, isbn):
    if library[isbn]["available"]:
      book= library[isbn]["available"]
      book=True
    print(f"{isbn} has been returned")

def display_books(library):
    for index,(isbn , book) in enumerate(library.items(),start=1):
      print(f"{index}.Title: {book['title']} Author:{book['author']} {'available' if book['available'] else'Chech out'}")
