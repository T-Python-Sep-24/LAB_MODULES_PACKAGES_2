def add_book(library:dict, title:str, author:str, isbn:str):
    if isbn in library:
        print("the book already exsist")
    else:
        library[isbn]={
            "title":title,
            "author":author,
            "available":True
        } 
        print("the book added seccessfuly")   

def remove_book(library, isbn):
    if isbn in library:
      del library[isbn]
      print("the book deleted seccessfuly") 
    else:
        print("the book already not exsist")

def check_out_book(library, isbn):
    if isbn in library:
        book=library[isbn]
        book["available"]=False
        print("the book checked out seccessfuly")

def return_book(library, isbn):
        if isbn in library:
            book=library[isbn]
            book["available"]=True
            print("the book returned seccessfuly")

def display_books(library):
    for isbn,book in library.items():
        print(f"{book["title"]} by {book["author"]} (ISBN: {isbn}) - {'Available' if book["available"] else 'Checked Out'}")

