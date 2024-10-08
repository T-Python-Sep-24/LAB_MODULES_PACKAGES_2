
def add_book(library:dict, title:str, author:str, isbn:str):
    if isbn in library:
        print(f'The book already exist! with ISBN: {isbn}')
    else:
        book = {}
        book.update({
            "title": title,
            "author": author,
            "isbn": isbn,
            "available": True 
        })
        
        library[isbn] = book
        
def remove_book(library:dict, isbn:str):
    if isbn in library:
        del library[isbn]
    else:
        print(f'The book does not exist! with ISBN: {isbn}')
        
def check_out_book(library:dict, isbn:str):
    if isbn in library:
        library[isbn]['available'] = False
    else:
        print(f'The book does not exist! with ISBN: {isbn}')
        
def return_book(library:dict, isbn:str):
    if isbn in library:
        library[isbn]['available'] = True
    else:
        print(f'The book does not exist! with ISBN: {isbn}')
        
def display_books(library:dict):
    print()
    print('Library books: ')
    for i, book in zip(range(len(list(library.keys()))), library.values()):
        print('Book number: ', i)
        if book['available']:
            print(f'{book['title']} by {book['author']} (ISBN: {book['isbn']}) - Available')
        else:
            print(f'{book['title']} by {book['author']} (ISBN: {book['isbn']}) - Checked Out')


        