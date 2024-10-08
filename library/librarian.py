
def add_book(library, title, author, isbn):
    if isbn in library:
        print(f" the ISBN ({isbn}) exists in the library")
    else:
        library[isbn] = {
            'title'  :title,
            'author':author,
            'isbn' : isbn,
            'available' : True
                    }
    

def remove_book(library, isbn):
    if isbn in library:
        book_pop=library.pop(isbn, None)
        print(f"Removed the book {book_pop} from the library.") 
    else:
        print(f'con not remove the ISBN ({isbn}) not exist')


def check_out_book(library, isbn):
    if isbn in library:
        library[isbn]['available'] = False
        print('Done check out book')
    else:
        print(f'The ISBN( {isbn} ) does not exist in the library')

def return_book(library, isbn):
    if isbn in library:
        library[isbn]['available'] = True
        print('Done return book')
    else:
        print(f'The ISBN( {isbn} ) does not exist in the library')

def display_books(library):
    for book in library.values():
        availability = "Available" if book['available'] else "Checked Out"
        print(f"{book['title']} by {book['author']} (ISBN: {book['isbn']}) -  {availability}")





