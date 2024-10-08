
def add_book(library, title, author, isbn):
    
    if isbn in library:
        print("this book already exists .")
    else:
        library[isbn] = {
            'title':str(title),
            'author':str(author),
            'isbn':str(isbn),
            'available': True
        }
        print("book added to the library")

def remove_book(library, isbn):

    if isbn in library:
        del library[isbn]
        print(" the book has been removed")
    else:
        print("book not found ")

def check_out_book(library, isbn):

    if isbn in library:
        if library[isbn]['available']:
            library[isbn]['available']= False
            print("checked out")
        else:
            print("not available")
    else:
        print("not found ")

def return_book(library, isbn):

    if isbn in library:
       library[isbn]['available'] = True
       print("its available")
        
    else: 
        print("not found")

def display_books(library):
    if not library:
        print("No books in library.")
        return
    
    for isbn in library:
          book = library[isbn]  
          available = "available" if book['available'] else "check out"
          print("{} by {} (ISBN : {}) - {}".format(book['title'],book['author'],isbn,available))
          