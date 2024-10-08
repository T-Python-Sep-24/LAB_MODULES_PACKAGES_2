#Lab 10 part 2

#Example
library = {}
#    "9780061120084": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "isbn": "9780061120084", "available": True},
#    "9780131103627": {"title": "The C Programming Language", "author": "Dennis Ritchie", "isbn": "9780131103627", "available": False}


#Add book Function
def add_book(library:dict, title:str, author:str, isbn:str):

    #Check if the isbn is the library dic
    if isbn in library:
        print("A book whith your ISBN Already Exists")
        return
    
    #New book dict
    new_book = {
        
        'Title': title,
        'Author': author,
        'ISBN': isbn,
        'Available': True

        }
    
    library[isbn] = new_book
    print(f"The Book '{title}' By '{author}' With the {isbn} Number, is Added Successfully.")




#Remove book Function
def remove_book(library, isbn):
    if isbn not in library:
        print("A Book Whith your ISBN Does Not Exists")
        return
    
    #Remove the book from the library
    del library [isbn]
    print(f"Book With ISBN {isbn} Has Been Removed Successfully.")
    


#Check Availablity Function
def check_out_book(library, isbn):
    if isbn not in library:
        print("A book whith your ISBN Does Not Exists")
        return
    
    if not library [isbn]['Available']:
        print("The book is not available")
        return
    
    # Set the 'available' status to False to indicate it is checked out
    library[isbn]['Available'] = False
    print(f"Book with ISBN {isbn} is available.")



def return_book(library, isbn):
     if isbn not in library:
        print("A book whith your ISBN Does Not Exists")
        return
     
     if library [isbn]['Available']:
        print("The book is already available in the library.")
        return
     
     # Set the 'available' status to True to indicate it is returned
     library[isbn]['Available'] = True
     print(f"Book with ISBN {isbn} has return and is available.")



def display_books(library):
    if not library:
        print("The library is currently empty.")
        return

    for isbn, book in library.items():
        title = book['Title']
        author = book['Author']
        available = "Available" if book['Available'] else "Checked Out"
        print(f"The {title} By {author} (ISBN: {isbn}) - {available}")


display_books(library) 
       
