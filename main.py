from LAB_MODULES_PACKAGES_2.library.librarian import add_book
from library import librarian
from library import librarian as lib
rary = {
    "1": {
        "title": "Hunter-X-Hunter",
        "author": "Togashi",
        'isbn':1,
        'available':True
    },
    "2": {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "isbn": 2,
        'available':True

    },
    "3": {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "isbn": 3,
        'available':True
    },
    "4": {
        "title": "1984",
        "author": "George Orwell",
        "isbn": 4,
        'available':True


    }
}

lib.add_book(rary,"python","Guido van Rossum",6)
lib.add_book(rary,"python","Guido van Rossum",5)
lib.add_book(rary,"python","Guido van Rossum",7)
lib.add_book(rary,"python","Guido van Rossum",9)
lib.check_out_book(rary,7)

lib.display_books(rary)
